---
name: update-listing
description: Update one existing Agentic Marketplace Listings record through Ready, Posted, price-change, Sold, or Closed lifecycle actions. Use when the seller wants to change the state or tracked posted or sold details of a known listing. Do not use for external posting, buyer communication, bookkeeping, or an ambiguous listing.
---
# AML: Update Listing
Update one unambiguous listing while keeping its folder location and tracked properties consistent.
## Locate the workspace and listing
Find the intended workspace by its `How to Use.md`, `Dashboard.base`, platform resources, and lifecycle folders. Read the plugin's [operating policy](../../references/operating-policy.md).

Resolve exactly one listing from an explicit path, the current `Listing.md`, or a sufficiently distinctive item name across all lifecycle folders. If more than one candidate matches, show the candidates and ask which one. Do not update or move anything until the listing is unambiguous.
## Determine the requested action
Support these v1 actions:
- **Ready:** move the whole item folder from Building to Ready after the seller confirms the draft is ready.
- **Posted:** require the actual posted price and posting date, write them to `posted_price` and `posted_date`, and move the whole item folder to Posted.
- **Price change:** require the new current posted price, replace `posted_price`, and keep the listing in Posted. V1 does not preserve price history.
- **Sold:** require the actual sold price and sold date, write them to `sold_price` and `sold_date`, and move the whole item folder to Sold.
- **Closed:** confirm that the listing ended without a sale and move the whole item folder to Closed. Do not populate sold properties.

Use unquoted `YYYY-MM-DD` values for dates and numeric values for prices. Preserve all unrelated properties, body content, photos, and item-folder contents.
## Preflight and authority
Before writing, show the exact `Listing.md`, current and target lifecycle folders, property changes, and folder move. Obtain explicit approval unless the user's current request already states the exact listing, action, and required price/date values. Posting means recording a seller-confirmed external event; this skill never posts to a marketplace.

Refuse an invalid transition that would contradict known state. If correcting mistaken data or reopening a Sold or Closed listing, show the inconsistency and obtain explicit approval for the correction.
## Apply and verify
Update the approved properties first, then move the whole item folder when the action changes lifecycle. Stop if the target item folder already exists. Verify that there is exactly one resulting item folder, that `Listing.md` retains its unrelated content, and that the parent lifecycle folder matches the action. `Dashboard.base` updates live and must not be regenerated.

Report the exact resulting path, property changes, lifecycle change, and smallest useful next action. Never post externally, contact buyers, accept an offer, or create another listing.
