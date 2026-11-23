# Troubleshooting

Find the symptom, check the causes in order (most common first), and change one thing at a time. Always rule out tracking and website problems before blaming the ads.

## Contents
- Ads not delivering or not spending
- CPM is high or rising
- CTR is low
- Clicks but no conversions
- CPA rose suddenly
- Performance fading slowly
- Learning limited
- Results unstable day to day
- Lead quality is poor
- Reported ROAS good, bank balance disagrees
- Cost cap or ROAS goal campaign will not spend
- New account struggles

## Ads not delivering or not spending

1. Ad status: in review, rejected, or "not delivering" with an error message. Read the message.
2. Account level: payment failure, account spending limit reached, account or page restriction (Account Quality).
3. Campaign or ad set switched off, scheduled for the future, or lifetime budget already used.
4. Bid controls too tight: a cost cap or bid cap below what the auction requires. Raise it or return to highest volume.
5. Audience too small: narrow retargeting, tight geography, heavy exclusions.
6. Budget too low for the market's CPM and CPA.
7. Conversion event not firing or pixel inactive, so the system has nothing to optimise toward.
8. Too many ads sharing a small budget.

## CPM is high or rising

CPM is the price of attention. It reflects competition and how much the system values the ad.
1. Season and competition: holidays, sales periods and month-ends raise everyone's CPM. Compare year on year.
2. Small or saturated audience: check frequency and reach. Widen the audience.
3. Weak ad quality signals: low engagement or negative feedback (hides, reports). Check the quality, engagement and conversion ranking diagnostics. Replace creative.
4. Restricted placements. Return to Advantage+ placements.
5. Expensive audience by nature: high-income countries, B2B, narrow age ranges.
6. Retargeting always has higher CPMs than prospecting; judge it on CPA.

A high CPM is acceptable when CPA is on target. Do not chase a cheaper CPM at the cost of buyer quality.

## CTR is low

1. The hook or first frame does not stop the scroll. Check hook rate; test new openings.
2. The message is unclear or generic. One idea per ad, stated concretely.
3. Wrong audience for the message, or an audience that has seen it too often.
4. Format mismatch: a landscape video squeezed into vertical placements, unreadable text.
5. Weak or missing call to action.

Check that you are reading link CTR, not CTR (all), which counts every tap.

## Clicks but no conversions

1. Tracking: are conversions happening but not recorded? Compare with real orders. Test the event.
2. Landing page views far below link clicks: slow load, redirects, broken link, in-app browser issue.
3. Message mismatch: the page does not continue the promise, price or product shown in the ad.
4. Page problems: slow mobile experience, confusing layout, no trust signals (reviews, guarantee, contact details), surprise costs at checkout, limited payment or delivery options.
5. Offer problem: the price or proposition is not compelling. No ad fixes that.
6. Wrong optimisation event: Traffic or Engagement campaigns bringing clickers, not buyers.
7. Low-quality placements driving accidental clicks: check the placement breakdown.

Locate the drop: view content → add to cart → initiate checkout → purchase. The step with the steepest fall is where to work.

## CPA rose suddenly

Ask what changed, in this order:
1. **Tracking or site**: events dropped, checkout error, stock ran out, page edited, price changed, app or theme update.
2. **Your own edits**: budget jump, new ads, audience or bid changes that restarted learning.
3. **The auction**: holiday, competitor sale, CPM spike. Compare CPM day by day.
4. **Creative**: the main ad fatigued. Check frequency and CTR trend for the top spender.
5. **Platform incident**: delivery or reporting issues affecting many advertisers. Check Meta's status page.
6. **Noise**: one or two bad days on low volume. Look at 7 days before reacting.

Break the change into parts: CPA = CPM / (1000 x CTR x conversion rate). Whichever component moved tells you where the cause sits (CPM: auction or audience; CTR: creative; conversion rate: site, offer or traffic quality).

## Performance fading slowly

Usually creative fatigue or audience saturation: frequency rising, CTR drifting down, first-time impression share falling. Introduce new concepts, widen audiences, refresh the offer. Check also for slow tracking decay (falling Event Match Quality, missing server events).

## Learning limited

Too few optimisation events for the ad set. Options: merge ad sets, raise the budget, broaden targeting and placements, reduce the number of ads, or optimise for a more frequent event. If the ad set is profitable, the label alone is not a reason to change anything.

## Results unstable day to day

Normal at low conversion volume. Reduce noise by consolidating, judging on 7-day windows, avoiding frequent edits, and keeping budgets steady. If one ad set swings between extremes, its budget is probably too small relative to CPA.

## Lead quality is poor

1. Instant forms with pre-filled fields are too easy: switch to the higher-intent form type, add a qualifying question or two, require a manually entered phone or email, add a review screen.
2. The ad over-promises or is vague about price and requirements: say who it is for and what it costs or requires.
3. Slow follow-up: leads contacted within minutes convert far better than those contacted the next day.
4. Optimising for raw leads: send qualified-lead events back and optimise for those.
5. Placement mix: check lead quality by placement and exclude poor sources with evidence.
6. Try a landing page form instead of an instant form; volume falls, intent rises.

## Reported ROAS good, bank balance disagrees

1. Double-counted purchases (deduplication failure).
2. Heavy view-through or retargeting credit for sales that would have happened anyway. Compare 1-day click, and check new-customer numbers.
3. ROAS judged without margin, discounts, shipping, returns, cancelled or undelivered cash-on-delivery orders, fees.
4. Break-even ROAS never calculated. See `benchmarks-and-formulas.md`.
Use MER and contribution margin as the decision numbers.

## Cost cap or ROAS goal campaign will not spend

The goal is tighter than the auction allows. Set the cap near the recent real CPA (or ROAS goal near the recent real ROAS), allow a few days, then tighten in small steps. Give it enough budget and audience. If it still will not spend, the creative or offer cannot hit that cost at volume.

## New account struggles

New accounts and pixels have no history, limited daily spend at first, and stricter review. Start with a simple structure, a modest budget raised gradually, policy-safe creative, and a verified business with two-factor authentication. Seed learning with first-party data (customer list) if available. Expect two to four weeks before results stabilise.
