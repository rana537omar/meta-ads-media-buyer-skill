# Campaign structure, objectives, budgets, bidding and audiences

## Contents
1. Choosing the objective and conversion event
2. Account structure by situation
3. Budgets
4. Bid strategies
5. Audiences and targeting
6. Placements
7. Launch checklist

## 1. Objective and conversion event

Meta delivers what you ask for, literally. A Traffic campaign finds people who click, not people who buy. Pick the objective that matches the real business outcome, then the deepest conversion event that still fires often enough.

| Business goal | Objective | Conversion location and event |
|---|---|---|
| Online sales | Sales | Website: Purchase. Use a catalog for many products |
| Leads for a sales team | Leads | Instant form (cheaper, lower intent) or website form: Lead (higher intent). Optimise for qualified leads if the CRM sends them back |
| Conversations that close in chat | Sales or Leads or Engagement | Messaging apps: WhatsApp, Messenger, Instagram Direct. Optimise for conversations, or for purchases through messaging where available |
| Booked calls or appointments | Leads or Sales | Website: Schedule or a custom booking event; or calls |
| App growth | App promotion | Installs or an in-app event |
| Local awareness, launches, large audiences | Awareness | Reach or ad recall |
| Building warm audiences cheaply | Engagement | Video views (ThruPlay), then retarget viewers |

**The volume rule.** An ad set learns best with roughly 50 optimisation events in a 7-day window. If Purchase cannot reach that at the available budget, either consolidate ad sets, raise the budget, or temporarily optimise one step up the funnel (Initiate Checkout, then Add to Cart). Move down again as soon as volume allows, because upper-funnel events bring lower-intent people.

Avoid Traffic and Engagement objectives when the goal is sales or leads. They are cheap per click and expensive per customer.

## 2. Account structure by situation

Default to the simplest structure that answers the business's questions. Every extra campaign or ad set divides budget and conversion data.

**New account or small budget (cannot fund 50 conversions a week in more than one ad set)**
- One Sales (or Leads) campaign, campaign-level budget.
- One ad set, broad targeting: country or region, age range only where legally or commercially required, existing customers excluded if the list exists.
- Three to six clearly different creatives.
- Add retargeting only when warm audiences are large enough to spend against (usually thousands of people, not hundreds).

**Established e-commerce**
- *Scaling campaign*: Advantage+ sales campaign or one broad ad set, holding the proven winners. Most of the budget (about 70 to 80 percent).
- *Creative testing campaign*: separate budget (about 10 to 20 percent), new concepts launched in batches. Winners are moved or duplicated into the scaling campaign.
- *Retention or catalog campaign* (optional): dynamic product ads to viewers and cart abandoners, or offers to past customers, when the audience size justifies it.

**Lead generation**
- One campaign per offer or service line, not per audience.
- Test instant form against landing page. Use higher-intent form settings and qualifying questions when lead quality is the complaint.
- Feed lead outcomes back (CRM integration or offline conversions) so delivery can optimise toward qualified leads.

**Local business**
- Radius or city targeting around the location, wide age range, no interest stacking: the geography already narrows the audience.
- Objectives: leads, calls, messages, or store traffic. Reach with frequency control can work for very small areas.

**Messaging-led and cash-on-delivery markets**
- Click-to-WhatsApp or Messenger ads with a short qualifying welcome flow.
- Track the stages that happen in chat (qualified, ordered, delivered) in a sheet or CRM, because reported "conversations" are not sales. Judge ads on cost per confirmed or delivered order.

**When separate campaigns or ad sets are justified**
- Different countries with different economics, languages or currencies.
- Different products with different margins or funnels.
- Prospecting versus existing customers, when their targets differ.
- A deliberate test with its own budget.

## 3. Budgets

- **Campaign budget (Advantage campaign budget, formerly CBO)**: Meta distributes spend across ad sets. Best for scaling and for consolidated structures.
- **Ad set budgets (ABO)**: you fix spend per ad set. Useful for controlled tests where each variant must get a fair share.
- **Minimum useful budget per ad set**: roughly (target CPA x 50) / 7 per day to exit learning. If that is unaffordable, expect "learning limited" and compensate by consolidating rather than by worrying about the label.
- **Testing budget per creative**: plan for about 1 to 3 times target CPA of spend per creative before judging it, more for expensive conversions.
- **Daily versus lifetime**: daily for always-on campaigns. Lifetime for fixed-date promotions or when ad scheduling is needed.

Tell the user what a budget can realistically buy. Example: a 20 per day budget with a 40 CPA yields about 3 to 4 conversions a week. That is too little for stable optimisation on Purchase, so recommend one ad set, few creatives and patience, or a shallower event.

## 4. Bid strategies

| Strategy | Use when | Watch out for |
|---|---|---|
| Highest volume (default, no cap) | Almost always the starting point; testing; limited data | Costs can rise as budgets scale |
| Cost per result goal (cost cap) | The CPA target is firm and there is conversion history | Set too low and delivery stalls. Start near the recent actual CPA, then tighten |
| ROAS goal (minimum ROAS) | Purchase values vary a lot and value tracking is reliable | Needs accurate value data; under-delivers if the goal is unrealistic |
| Bid cap | Experienced buyers controlling the auction bid directly | Easy to choke delivery; not for beginners |
| Highest value | Maximising revenue with reliable purchase values | Can favour few large orders |

Caps are guard rails for scaling, not a fix for a weak offer or creative.

## 5. Audiences and targeting

**Broad first.** In most accounts with working conversion tracking, broad targeting (location, age, sometimes gender) with strong creative matches or beats detailed targeting, because the system finds buyers from conversion signals and from who responds to each ad. Advantage+ audience treats most inputs as suggestions rather than limits.

**When to narrow**
- New pixel with no conversion history: interests or lookalikes can give delivery a starting direction.
- Genuinely niche B2B or specialist products.
- Legal or commercial limits (age-restricted goods, service areas).
- Small budgets in very large countries.

**Custom audiences (first-party data)**
- Customer list (hashed emails and phones), website visitors by recency and page, add-to-cart and checkout abandoners, video viewers, page and profile engagers, lead form openers, app users.
- Uses: exclusions (do not pay to reach yesterday's buyers with a prospecting offer), retargeting, lookalike seeds, and audience suggestions.

**Lookalikes**
- Seed quality matters more than size: purchasers or high-value customers beat all visitors. 1 percent is closest; larger percentages trade similarity for reach. Their edge over broad has shrunk, so test rather than assume.

**Retargeting**
- Worth a separate ad set only when the audience is big enough. A common split: recent high intent (cart and checkout, 7 to 14 days) and wider warm (visitors and engagers, 30 to 180 days).
- Use different messages from prospecting: objections, proof, guarantees, reminders, offers.
- Watch frequency; small audiences saturate quickly.

**Exclusions and overlap**
- Exclude purchasers from prospecting where it matters commercially. Avoid several ad sets chasing the same people; overlapping ad sets from the same account do not bid against each other in the same auction, but they do split learning and inflate frequency.

**Special ad categories** (housing, employment, financial products and services, social issues, elections or politics) restrict age, gender, postcode and lookalike targeting. Declare them; see `policy-and-compliance.md`.

## 6. Placements

Use Advantage+ placements by default: more inventory generally lowers cost per result. Restrict placements only with evidence (for example, lead quality from Audience Network is poor) or when the creative genuinely cannot run somewhere. Supply assets in 4:5 or 1:1 for feeds and 9:16 for Stories and Reels so every placement looks native.

## 7. Launch checklist

- [ ] Pixel and Conversions API firing, the conversion event verified in Events Manager with a real test
- [ ] Domain verified; events deduplicated (same event ID from browser and server)
- [ ] Correct objective, conversion location and event; attribution setting chosen deliberately
- [ ] Budget, schedule, currency and time zone correct
- [ ] Locations, ages, languages and exclusions correct; special ad category declared if relevant
- [ ] Each ad: right page and Instagram account, correct URL, UTMs added, CTA matches the page
- [ ] Creative previews checked on feed, Stories and Reels; text inside safe zones
- [ ] Landing page loads fast on mobile and matches the ad's promise
- [ ] Names follow the naming convention
- [ ] Payment method works and the account spending limit will not cut delivery
- [ ] Review plan agreed: when to check, what counts as a pass or fail
