#!/usr/bin/env python3
"""Analyse a Meta Ads Manager CSV export and print a markdown performance report.

Usage:
    python analyze_ads.py export.csv
    python analyze_ads.py export.csv --target-cpa 25
    python analyze_ads.py export.csv --target-roas 2.5 --level adset --top 15

Standard library only. Recognises the usual Ads Manager column names (English
exports); unrecognised columns are ignored and missing ones are reported.
"""
import argparse
import csv
import io
import re
import sys
from collections import OrderedDict

# metric key -> regex patterns tried in order against lower-cased headers
COLUMNS = OrderedDict([
    ("spend", [r"^amount spent", r"^spend\b", r"^cost$"]),
    ("impressions", [r"^impressions$"]),
    ("reach", [r"^reach$"]),
    ("link_clicks", [r"^link clicks$", r"^outbound clicks$", r"^clicks \(all\)$"]),
    ("lpv", [r"^landing page views$", r"^website landing page views$"]),
    ("plays_3s", [r"^3-second video plays$", r"^video plays at 3"]),
    ("thruplays", [r"^thruplays$"]),
    ("atc", [r"^adds to cart$", r"^website adds to cart$"]),
    ("checkouts", [r"^checkouts initiated$", r"^website checkouts initiated$"]),
    ("purchases", [r"^purchases$", r"^website purchases$"]),
    ("value", [r"^purchases conversion value$", r"^purchase conversion value$",
               r"^website purchases conversion value$", r"conversion value$"]),
    ("leads", [r"^leads$", r"^on-facebook leads$", r"^website leads$"]),
    ("messages", [r"^messaging conversations started$"]),
    ("results", [r"^results$"]),
])
NAME_COLUMNS = {
    "campaign": [r"^campaign name$", r"^campaign$"],
    "adset": [r"^ad set name$", r"^ad set$", r"^adset name$"],
    "ad": [r"^ad name$", r"^ad$"],
}
CONVERSION_PRIORITY = ["purchases", "leads", "messages", "results"]
CONVERSION_LABEL = {"purchases": "Purchases", "leads": "Leads",
                    "messages": "Conversations", "results": "Results"}


def to_number(raw):
    if raw is None:
        return 0.0
    text = re.sub(r"[^\d.\-]", "", str(raw).replace(",", ""))
    try:
        return float(text) if text not in ("", "-", ".") else 0.0
    except ValueError:
        return 0.0


def find_column(headers, patterns):
    lowered = [(h, h.strip().lower()) for h in headers if h]
    for pattern in patterns:
        for original, low in lowered:
            if re.search(pattern, low):
                return original
    return None


def div(a, b):
    return a / b if b else None


def fmt(value, kind="num"):
    if value is None:
        return "-"
    if kind == "pct":
        return f"{value * 100:.2f}%"
    if kind == "money":
        return f"{value:,.2f}"
    if kind == "int":
        return f"{value:,.0f}"
    return f"{value:,.2f}"


def metrics(t, conv_key):
    conv = t.get(conv_key, 0.0)
    return {
        "spend": t["spend"], "impressions": t["impressions"], "conv": conv,
        "cpm": div(t["spend"] * 1000, t["impressions"]),
        "ctr": div(t["link_clicks"], t["impressions"]),
        "cpc": div(t["spend"], t["link_clicks"]),
        "lpv_rate": div(t["lpv"], t["link_clicks"]) if t["lpv"] else None,
        "cvr": div(conv, t["lpv"] or t["link_clicks"]),
        "cpa": div(t["spend"], conv),
        "roas": div(t["value"], t["spend"]) if t["value"] else None,
        "freq": div(t["impressions"], t["reach"]) if t["reach"] else None,
        # hook rate uses impressions of video rows only, so image ads do not dilute it
        "hook": div(t["plays_3s"], t.get("video_impr") or t["impressions"])
        if t["plays_3s"] else None,
        "hold": div(t["thruplays"], t["plays_3s"]) if t["plays_3s"] else None,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("csv_path", help="Ads Manager export (.csv)")
    parser.add_argument("--target-cpa", type=float, help="target cost per conversion")
    parser.add_argument("--target-roas", type=float, help="target ROAS, e.g. 2.5")
    parser.add_argument("--level", choices=["ad", "adset", "campaign"],
                        help="aggregation level (default: lowest level in the file)")
    parser.add_argument("--conversion", choices=CONVERSION_PRIORITY,
                        help="conversion metric to judge on (default: auto)")
    parser.add_argument("--top", type=int, default=20, help="rows to show (default 20)")
    args = parser.parse_args()

    with open(args.csv_path, "rb") as handle:
        raw = handle.read()
    for encoding in ("utf-8-sig", "utf-16", "cp1252"):
        try:
            text = raw.decode(encoding)
            break
        except UnicodeError:
            continue
    sample = text[:4096]
    delimiter = "\t" if sample.count("\t") > sample.count(",") else ","
    reader = csv.DictReader(io.StringIO(text), delimiter=delimiter)
    headers = reader.fieldnames or []
    rows = list(reader)
    if not rows:
        sys.exit("No data rows found in the file.")

    col = {key: find_column(headers, pats) for key, pats in COLUMNS.items()}
    names = {key: find_column(headers, pats) for key, pats in NAME_COLUMNS.items()}
    if not col["spend"] or not col["impressions"]:
        sys.exit("The export needs at least 'Amount spent' and 'Impressions' columns. "
                 f"Columns found: {', '.join(h for h in headers if h)}")

    level = args.level or next((l for l in ("ad", "adset", "campaign") if names[l]), None)
    if level and not names[level]:
        sys.exit(f"No name column for level '{level}' in this export.")
    path = [l for l in ("campaign", "adset", "ad") if names[l]]
    if level:
        path = path[: path.index(level) + 1]

    groups = OrderedDict()
    total = {key: 0.0 for key in COLUMNS}
    for row in rows:
        label = " > ".join((row.get(names[l]) or "").strip() for l in path) or "All"
        if not label.replace(">", "").strip():
            continue  # summary/total row without names
        bucket = groups.setdefault(label, {key: 0.0 for key in COLUMNS})
        for key, header in col.items():
            if header:
                value = to_number(row.get(header))
                bucket[key] += value
                total[key] += value
        if col["plays_3s"] and to_number(row.get(col["plays_3s"])) > 0:
            impressions = to_number(row.get(col["impressions"]))
            bucket["video_impr"] = bucket.get("video_impr", 0.0) + impressions
            total["video_impr"] = total.get("video_impr", 0.0) + impressions

    conv_key = args.conversion or next(
        (k for k in CONVERSION_PRIORITY if col[k] and total[k] > 0), "results")
    conv_label = CONVERSION_LABEL[conv_key]
    acct = metrics(total, conv_key)
    target_cpa = args.target_cpa
    if not target_cpa and args.target_roas and total["purchases"] and total["value"]:
        target_cpa = (total["value"] / total["purchases"]) / args.target_roas
    reference_cpa = target_cpa or acct["cpa"]

    out = []
    out.append(f"# Meta Ads analysis: {len(groups)} {level or 'row'}(s)\n")
    out.append(f"Conversion metric: **{conv_label}**. "
               + (f"Target CPA: **{fmt(target_cpa, 'money')}**. " if target_cpa else
                  "No target given: rows are compared with the account average CPA. ")
               + (f"Target ROAS: **{args.target_roas}**." if args.target_roas else "") + "\n")

    out.append("## Account totals\n")
    out.append("| Spend | Impr. | CPM | Link CTR | CPC | LPV rate | CVR | "
               f"{conv_label} | CPA | ROAS | Freq. |")
    out.append("|---|---|---|---|---|---|---|---|---|---|---|")
    out.append("| " + " | ".join([
        fmt(acct["spend"], "money"), fmt(acct["impressions"], "int"), fmt(acct["cpm"], "money"),
        fmt(acct["ctr"], "pct"), fmt(acct["cpc"], "money"), fmt(acct["lpv_rate"], "pct"),
        fmt(acct["cvr"], "pct"), fmt(acct["conv"], "int"), fmt(acct["cpa"], "money"),
        fmt(acct["roas"]), fmt(acct["freq"])]) + " |\n")

    funnel = [("Impressions", total["impressions"]), ("Link clicks", total["link_clicks"]),
              ("Landing page views", total["lpv"]), ("Adds to cart", total["atc"]),
              ("Checkouts initiated", total["checkouts"]), (conv_label, total[conv_key])]
    funnel = [(n, v) for n, v in funnel if v]
    if len(funnel) > 2:
        out.append("## Funnel\n")
        out.append("| Stage | Count | Rate from previous stage |")
        out.append("|---|---|---|")
        previous = None
        for name, value in funnel:
            rate = fmt(div(value, previous), "pct") if previous else "-"
            out.append(f"| {name} | {fmt(value, 'int')} | {rate} |")
            previous = value
        out.append("")

    ranked = sorted(groups.items(), key=lambda kv: kv[1]["spend"], reverse=True)
    out.append(f"## By {level or 'row'} (top {min(args.top, len(ranked))} by spend)\n")
    out.append(f"| Name | Spend | CPM | Link CTR | Hook | LPV rate | {conv_label} | "
               "CPA | ROAS | Freq. |")
    out.append("|---|---|---|---|---|---|---|---|---|---|")
    flags = {"cut": [], "fix": [], "scale": [], "watch": []}
    for index, (label, bucket) in enumerate(ranked):
        m = metrics(bucket, conv_key)
        if index < args.top:
            out.append("| " + " | ".join([
                label, fmt(m["spend"], "money"), fmt(m["cpm"], "money"), fmt(m["ctr"], "pct"),
                fmt(m["hook"], "pct"), fmt(m["lpv_rate"], "pct"), fmt(m["conv"], "int"),
                fmt(m["cpa"], "money"), fmt(m["roas"]), fmt(m["freq"])]) + " |")
        if reference_cpa:
            if m["conv"] == 0 and m["spend"] >= 2 * reference_cpa:
                flags["cut"].append(f"**{label}**: spent {fmt(m['spend'], 'money')} "
                                    f"({m['spend'] / reference_cpa:.1f}x reference CPA) with no "
                                    f"{conv_label.lower()}.")
            elif m["cpa"] and m["cpa"] > 1.5 * reference_cpa and m["spend"] >= 3 * reference_cpa:
                flags["cut"].append(f"**{label}**: CPA {fmt(m['cpa'], 'money')} is "
                                    f"{m['cpa'] / reference_cpa:.1f}x the reference after "
                                    f"{fmt(m['spend'], 'money')} spend.")
            elif m["cpa"] and m["cpa"] <= 0.8 * reference_cpa and m["conv"] >= 5:
                flags["scale"].append(f"**{label}**: CPA {fmt(m['cpa'], 'money')} "
                                      f"({m['cpa'] / reference_cpa:.0%} of reference) on "
                                      f"{fmt(m['conv'], 'int')} {conv_label.lower()}.")
            elif m["cpa"] and m["cpa"] <= 0.8 * reference_cpa:
                flags["watch"].append(f"**{label}**: promising CPA {fmt(m['cpa'], 'money')} but "
                                      f"only {fmt(m['conv'], 'int')} {conv_label.lower()}; "
                                      "needs more data.")
        if args.target_roas and m["roas"] and m["roas"] >= 1.2 * args.target_roas \
                and bucket["purchases"] >= 5:
            note = f"**{label}**: ROAS {fmt(m['roas'])} vs target {args.target_roas}."
            if not any(label in existing for existing in flags["scale"]):
                flags["scale"].append(note)
        if m["impressions"] >= 2000:
            if acct["ctr"] and m["ctr"] is not None and m["ctr"] < 0.5 * acct["ctr"]:
                flags["fix"].append(f"**{label}**: link CTR {fmt(m['ctr'], 'pct')} is under half "
                                    f"the account average ({fmt(acct['ctr'], 'pct')}): weak "
                                    "message or hook.")
            if m["hook"] is not None and m["hook"] < 0.20:
                flags["fix"].append(f"**{label}**: hook rate {fmt(m['hook'], 'pct')} is below "
                                    "20%: rework the first three seconds.")
        if m["lpv_rate"] is not None and bucket["link_clicks"] >= 50 and m["lpv_rate"] < 0.6:
            flags["fix"].append(f"**{label}**: only {fmt(m['lpv_rate'], 'pct')} of link clicks "
                                "become landing page views: check page speed, redirects, tracking.")
        if m["freq"] and m["freq"] > 3.5:
            flags["watch"].append(f"**{label}**: frequency {fmt(m['freq'])}: check for fatigue "
                                  "(falling CTR, rising CPA) or a small audience.")
    out.append("")

    out.append("## Flags\n")
    titles = [("cut", "Cut candidates"), ("fix", "Fix"), ("scale", "Scale candidates"),
              ("watch", "Watch")]
    any_flag = False
    for key, title in titles:
        if flags[key]:
            any_flag = True
            out.append(f"### {title}")
            out.extend(f"- {line}" for line in flags[key])
            out.append("")
    if not any_flag:
        out.append("No rows crossed the flag thresholds.\n")

    missing = [key for key in ("link_clicks", "reach", "lpv", "plays_3s", "value")
               if not col[key]]
    notes = ["Flags are rule-of-thumb thresholds. Check sample size, date range and real "
             "business revenue before acting."]
    if missing:
        friendly = {"link_clicks": "Link clicks", "reach": "Reach", "lpv": "Landing page views",
                    "plays_3s": "3-second video plays", "value": "Purchases conversion value"}
        notes.append("Columns not found (related metrics show '-'): "
                     + ", ".join(friendly[key] for key in missing) + ".")
    if acct["conv"] and acct["conv"] < 30:
        notes.append(f"Only {fmt(acct['conv'], 'int')} {conv_label.lower()} in total: "
                     "conclusions at row level are weak.")
    out.append("## Notes\n")
    out.extend(f"- {note}" for note in notes)

    sys.stdout.reconfigure(encoding="utf-8")
    print("\n".join(out))


if __name__ == "__main__":
    main()
