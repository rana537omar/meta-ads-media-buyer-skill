# Formulas, targets, forecasts and benchmarks

## Contents
1. Metric formulas
2. Break-even and targets
3. Lead generation maths
4. Forecasting
5. Budget sizing
6. Benchmarks and how to use them

## 1. Metric formulas

| Metric | Formula |
|---|---|
| CPM | spend / impressions x 1000 |
| Link CTR | link clicks / impressions |
| CPC (link) | spend / link clicks |
| Landing page view rate | landing page views / link clicks |
| Conversion rate (CVR) | conversions / landing page views (or / link clicks; say which) |
| CPA (cost per result) | spend / conversions |
| ROAS | conversion value / spend |
| AOV | revenue / orders |
| Frequency | impressions / reach |
| Hook rate | 3-second video plays / impressions |
| Hold rate | ThruPlays / 3-second video plays |
| MER | total revenue / total ad spend (all channels) |
| CAC | total acquisition spend / new customers |
| LTV | average order value x orders per customer over the period x gross margin |

Useful identity for diagnosis:

```
CPA = CPM / (1000 x CTR x CVR)        ROAS = AOV / CPA
```

So halving CPA needs CTR or CVR to double, or CPM to halve, or a mix. This shows which lever is realistic.

## 2. Break-even and targets (e-commerce)

Work with contribution margin: what is left from an order after product cost, shipping, payment fees, packaging, and expected returns or failed deliveries, before ad spend.

```
Margin %            = (AOV - variable costs per order) / AOV
Break-even ROAS     = 1 / margin %
Break-even CPA      = AOV x margin %
Target CPA          = break-even CPA x (1 - desired profit share)
Target ROAS         = AOV / target CPA
```

Example: AOV 60, variable costs 33 → margin 27 = 45 percent. Break-even ROAS = 1 / 0.45 = 2.22. Break-even CPA = 27. To keep a third of the margin as profit: target CPA = 18, target ROAS = 3.33.

Adjustments:
- **Cash on delivery or high return rates**: multiply revenue by the delivered or kept rate first. At a 75 percent delivery rate, effective AOV in the example is 45 and failed deliveries still cost shipping.
- **Repeat purchase businesses**: first-order break-even can be accepted or even exceeded if LTV repays it within a period the cash flow can stand. State the payback period explicitly.
- **Tax**: use revenue net of VAT or sales tax where the platform reports gross.

## 3. Lead generation maths

```
Max cost per lead        = profit per sale x lead-to-sale rate x share of profit you will spend
Cost per qualified lead  = spend / qualified leads
Cost per sale            = CPL / lead-to-sale rate
```

Example: profit per sale 800, 5 percent of leads become sales, willing to spend half the profit on acquisition → max CPL = 800 x 0.05 x 0.5 = 20.

For booked-call funnels, extend the chain: lead → booked → showed → closed, with a rate at each step. The weakest rate is often a sales process issue rather than an ads issue.

## 4. Forecasting

Build forecasts from assumptions and present low, expected and high cases. Never promise an outcome.

```
Impressions  = budget / CPM x 1000
Link clicks  = impressions x CTR
Conversions  = link clicks x CVR
Revenue      = conversions x AOV
CPA          = budget / conversions
ROAS         = revenue / budget
```

Example with 3,000 budget:

| Case | CPM | CTR | CVR (per click) | AOV | Conversions | CPA | ROAS |
|---|---|---|---|---|---|---|---|
| Low | 14 | 0.8% | 1.0% | 60 | 17 | 175 | 0.34 |
| Expected | 10 | 1.2% | 2.0% | 60 | 72 | 42 | 1.44 |
| High | 8 | 1.6% | 3.0% | 60 | 180 | 17 | 3.60 |

The spread shows how sensitive results are to CTR and conversion rate, which is why creative and landing page work matter more than settings. Take assumptions from the account's history when it exists; otherwise label them as assumptions and plan a test budget to replace them with real numbers.

## 5. Budget sizing

```
Daily budget to exit learning (per ad set)  ≈ target CPA x 50 / 7
Creative test budget                        ≈ number of concepts x 1 to 3 x target CPA
Minimum sensible test period                ≈ 7 to 14 days, covering whole weeks
```

If the user's budget is below what the formulas ask for, do not refuse to plan: consolidate into one ad set, test fewer creatives, optimise for a shallower event if needed, and set expectations about slower learning.

## 6. Benchmarks and how to use them

Rankings of usefulness: the account's own history, then the same business last year, then figures from the same country and industry, and only then generic global numbers. Use the rough ranges below only as a sanity check and say they are rough.

| Metric | Rough typical range | Notes |
|---|---|---|
| CPM | Under 2 to 5 in lower-cost markets; 8 to 25 or more in the US, UK, and similar markets (USD) | Peaks in Q4 and around major sales |
| Link CTR | 0.8 to 2 percent | Feeds higher than Stories; retargeting higher than prospecting |
| Hook rate | 20 to 35 percent | Below 20 percent: rework the opening |
| Hold rate | 20 to 40 percent of 3-second viewers | Depends strongly on video length |
| Landing page view rate | 70 to 90 percent of link clicks | Below 60 percent: page speed or tracking problem |
| E-commerce conversion rate | 1 to 3 percent of sessions | Higher for low prices, warm traffic, strong offers |
| Instant form conversion | 5 to 15 percent of clicks or more | Quality varies inversely with ease |
| Prospecting frequency (7 days) | 1 to 2.5 | Above 3 to 4 with falling CTR: fatigue |

A metric outside these ranges is a prompt to investigate, not a verdict. A 0.6 percent CTR with a profitable CPA is a good ad.
