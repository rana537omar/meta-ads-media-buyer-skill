# Tracking, attribution and measurement

Delivery optimises toward the events it receives. Missing, duplicated or wrong events mean the system chases the wrong people, and the reports mislead the buyer. Fix tracking before judging performance.

## Contents
1. The setup that every account needs
2. Standard events
3. Verifying that tracking works
4. Common tracking faults
5. Attribution settings
6. Why Ads Manager and other tools disagree
7. Measuring true impact
8. UTMs
9. Lead and offline outcomes
10. Privacy and consent

## 1. The setup every account needs

1. **Meta Pixel** on every page of the site (browser events).
2. **Conversions API (CAPI)** sending the same events from the server. Browser-only tracking loses events to ad blockers, browser privacy features and iOS restrictions. Use the platform's native integration (Shopify, WooCommerce, and similar), the Conversions API Gateway, server-side Google Tag Manager, or a direct integration.
3. **Deduplication**: pixel and server versions of an event must share the same event name and event ID, otherwise conversions are double counted.
4. **Customer information parameters** with each event (hashed email, phone, name, city, external ID, plus the click ID and browser ID cookies). These raise Event Match Quality, which improves attribution and optimisation. Aim for a score of roughly 6 or higher on key events, and as high as practical on Purchase.
5. **Purchase events carry value and currency**, and ideally content IDs matching the catalog.
6. **Domain verified** in Business settings, and the account's key events configured where Events Manager asks for it.
7. **Automatic advanced matching** switched on for the pixel.

## 2. Standard events

Use standard events where they fit, since optimisation and reporting understand them: PageView, ViewContent, Search, AddToCart, AddToWishlist, InitiateCheckout, AddPaymentInfo, Purchase, Lead, CompleteRegistration, Contact, Schedule, StartTrial, Subscribe, SubmitApplication. Use custom events or custom conversions for steps that have no standard equivalent, such as a qualified lead.

## 3. Verifying

- **Events Manager → Test events**: perform the action on the site and confirm each event arrives once from the browser and once from the server, marked as deduplicated.
- **Meta Pixel Helper** browser extension: shows events and parameters on a page.
- **Events Manager → Overview and Diagnostics**: warnings about missing parameters, deduplication, falling event volume or mismatched domains.
- **Reality check**: compare a week of Purchase events and value with the store's actual orders and revenue. Totals should be close (event counts include all traffic sources, not only ads).

## 4. Common faults

| Symptom | Likely cause |
|---|---|
| Purchases in Ads Manager about double real orders | Pixel and CAPI both firing without matching event IDs; event firing on page reload of the thank-you page |
| Purchases far below real orders | Pixel blocked and no CAPI; checkout on another domain; consent banner blocking; event only fires on a page some customers skip |
| ROAS absurdly high or zero | Value missing, wrong currency, or value sent in cents |
| Leads counted on page load | Event attached to the form page rather than the confirmation |
| Low Event Match Quality | Few customer parameters sent; missing click ID cookie |
| Sudden drop in events | Site theme or app update removed the code; tag manager change; expired access token for CAPI |
| Many link clicks, few landing page views | Slow page, redirects, in-app browser failures, or pixel not loading |

## 5. Attribution settings

The attribution setting on the ad set defines which conversions are credited and optimised for. The common default is 7-day click plus 1-day view (with engaged-view for video where offered). Options and defaults change; check what the ad set screen currently offers.

- Longer click windows suit considered purchases; 1-day click suits impulse buys and gives a stricter picture.
- View-through conversions inflate results for retargeting and for brands with heavy organic demand. Use the "compare attribution settings" columns to see how much of the result is view-through.
- Compare like with like: do not judge one campaign on 7-day click and another on 1-day click.
- Results keep arriving for days after the click. Yesterday's numbers are incomplete, so avoid hard decisions on the most recent one to three days for products with a delay between click and purchase.

## 6. Why the numbers disagree

Ads Manager, Google Analytics, the store platform and the CRM will never match exactly. Reasons:
- Different attribution models (Meta credits its own clicks and views; analytics tools often credit the last non-direct click).
- Meta reports by the date of the ad interaction; stores report by order date.
- Cross-device and in-app browser journeys that analytics tools cannot connect.
- Modelled conversions on Meta's side; consent and blocked cookies on the analytics side.
- View-through conversions, which analytics tools never see.

Do not try to force a match. Agree on one source of truth for decisions, usually the business's own revenue.

## 7. Measuring true impact

- **MER (marketing efficiency ratio)** = total revenue / total ad spend across all channels. Track it daily or weekly. If Meta spend rises and MER holds, the spend is doing real work.
- **New-customer CAC** = ad spend / new customers, and **new-customer ROAS**, where the business can separate new from returning buyers.
- **Post-purchase survey** ("Where did you hear about us?") as a cross-check.
- **Conversion lift or geo holdout tests** for larger budgets: the only way to measure incrementality directly.
- **Simple on/off evidence**: what happened to total sales when spend changed materially.

Retargeting and branded audiences usually show the best platform ROAS and the least incremental effect. Weigh them accordingly.

## 8. UTMs

Add URL parameters to every ad so analytics and the CRM can see the source. A dynamic template for the "URL parameters" field:

```
utm_source=meta&utm_medium=paid_social&utm_campaign={{campaign.name}}&utm_content={{ad.name}}&utm_term={{adset.name}}&utm_id={{campaign.id}}
```

Keep the format identical across all ads, and avoid spaces in names that will end up in URLs.

## 9. Leads and offline outcomes

For lead generation and messaging, the platform's "result" is only the start. Track lead → qualified → sale, with revenue.
- Connect the CRM (native integration, Zapier or Make, or the Conversions API for CRM events) so qualified and closed stages are sent back to Meta. Then optimise for the deeper event.
- Where integration is not possible, keep a sheet: date, ad name (from the UTM or form), lead status, sale value. Compute cost per qualified lead and cost per sale by ad weekly.
- For phone, store or cash-on-delivery sales, upload offline conversions or send them through CAPI.

## 10. Privacy and consent

Collect and send personal data only with a lawful basis. In regions with consent laws (GDPR in the EU and UK, and similar rules elsewhere), the pixel and CAPI should respect the visitor's consent choice through a consent management platform. Customer lists must come from people who gave their data to the business; never upload bought or scraped lists. Certain sensitive categories (for example health and financial data sources) face restrictions on which events can be shared with Meta. Check the data source's category in Events Manager when lower-funnel events appear blocked.
