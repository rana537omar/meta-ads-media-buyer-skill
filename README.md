# Meta Ads Media Buyer (Claude Skill)

A skill that turns Claude into a senior Meta Ads media buyer for Facebook, Instagram, Messenger and WhatsApp advertising. It plans and structures campaigns, writes creative and copy, audits accounts, analyses Ads Manager exports, diagnoses problems, guides scaling, and produces client-ready reports.

## What it does

| Area | Examples |
|---|---|
| Strategy and launch | Objective and event selection, account structure, budgets, bid strategies, audiences, launch checklist |
| Creative | Angles, hooks, video scripts, primary text and headlines, creative testing plans, briefs for designers and creators |
| Tracking | Pixel and Conversions API setup checks, deduplication, attribution settings, UTMs, reconciling Ads Manager with real revenue |
| Optimisation | Cut, keep or scale decisions with spend thresholds, learning phase handling, vertical and horizontal scaling |
| Troubleshooting | High CPM, low CTR, no delivery, CPA spikes, learning limited, fatigue, poor lead quality |
| Maths | Break-even ROAS and CPA, lead gen targets, forecasts with low, expected and high cases |
| Reporting | Audit reports, weekly and monthly client reports, naming conventions, intake questionnaire |
| Policy | Rejected ads, restricted accounts, special ad categories, compliant copy rewrites |
| Data analysis | A bundled script reads an Ads Manager CSV export and flags what to cut, fix and scale |

## Install

### Claude apps (claude.ai, desktop, mobile)

1. Download [`dist/meta-ads-media-buyer.zip`](dist/meta-ads-media-buyer.zip) (or the identical `.skill` file) from this repository, or zip the `meta-ads-media-buyer` folder yourself.
2. In Claude, open **Settings → Capabilities → Skills** and upload the file.
3. Switch the skill on. Code execution must be enabled for skills to work.

### Claude Code

Copy the skill folder into your skills directory:

```bash
git clone https://github.com/rana537omar/meta-ads-media-buyer-skill.git
cp -r meta-ads-media-buyer-skill/meta-ads-media-buyer ~/.claude/skills/
```

Use `.claude/skills/` inside a project instead if you want it for that project only.

## Use

Just ask. The skill loads on its own when a request is about Meta advertising. Examples:

- "I sell skincare online, average order 45 USD, 60 percent margin, 1,500 USD a month to spend. Build my launch plan."
- "Here is my Ads Manager export. What should I pause and what should I scale?" (attach the CSV)
- "Write 8 hooks and 2 UGC scripts for a meal-prep delivery service."
- "My CPA doubled this week. Help me find out why."
- "Audit this account and give me a 30-day action plan."
- "My ad was rejected for personal attributes. Rewrite it."
- "Create this month's client report from these numbers."

### Exporting data for analysis

In Ads Manager choose the ad level, add these columns, then **Export → CSV**: campaign name, ad set name, ad name, amount spent, impressions, reach, frequency, link clicks, landing page views, adds to cart, checkouts initiated, purchases (or leads), purchases conversion value, 3-second video plays, ThruPlays.

The analyzer can also be run on its own (Python 3, no dependencies):

```bash
python meta-ads-media-buyer/scripts/analyze_ads.py examples/sample-export.csv --target-cpa 25
```

## Contents

```
meta-ads-media-buyer/
├── SKILL.md                         Core workflow and operating principles
├── references/
│   ├── campaign-structure.md        Objectives, structure, budgets, bidding, audiences
│   ├── creative.md                  Angles, hooks, copy, testing, specs
│   ├── tracking-and-measurement.md  Pixel, Conversions API, attribution, UTMs
│   ├── optimization-and-scaling.md  Review rhythm, decision rules, scaling
│   ├── troubleshooting.md           Symptom-based diagnosis
│   ├── policy-and-compliance.md     Ad review, restrictions, special categories
│   ├── benchmarks-and-formulas.md   Break-even, targets, forecasts, benchmarks
│   └── templates.md                 Intake, naming, briefs, audit and report formats
└── scripts/
    └── analyze_ads.py               Ads Manager CSV analyzer
examples/
└── sample-export.csv                Sample data for trying the analyzer
```

## Notes

- The skill gives guidance and analysis. It does not connect to an ad account by itself. If you give Claude tools that can change a live account, the skill instructs it to confirm with you before anything that spends money.
- Meta changes its features and policies often. Confirm specifics such as specs, limits and policy wording in Ads Manager or Meta's Business Help Center.
- Advertising results depend on your product, offer, market and creative. Nothing here guarantees performance.
- The skill will not help with policy evasion, fake reviews or misleading claims.
- Not affiliated with or endorsed by Meta Platforms, Inc.

## License

MIT. See [LICENSE](LICENSE).
