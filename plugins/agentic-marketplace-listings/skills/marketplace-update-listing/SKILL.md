---
name: marketplace-update-listing
description: Update one existing Agentic Marketplace Listings record through Ready, Posted, price-change, Sold, or Closed lifecycle actions. Use when the seller wants to change the state or tracked posted or sold details of a known listing. Do not use for external posting, buyer communication, bookkeeping, or an ambiguous listing.
---
# Marketplace: Update Listing
Complete one unambiguous lifecycle update in the same turn whenever the seller has supplied everything the action requires.
## Fast preflight
Find the intended workspace by the presence of `How to Use.md`, `Dashboard.base`, platform resources, and the five lifecycle folders. Read the plugin's [operating policy](../../references/operating-policy.md).

In one read-only pass whenever practical:
1. verify the workspace markers without loading their contents;
2. resolve exactly one listing from an explicit path, the current `Listing.md`, or a sufficiently distinctive item name across all lifecycle folders;
3. read that listing's `Listing.md`; and
4. verify that a different item folder does not already occupy the target path.

Do not load templates, platform guidance, seller profiles, photos, prior listings, unrelated project history, `How to Use.md`, `Dashboard.base`, or web sources for a routine update. If more than one listing could match, show the candidates and ask which one. Do not update anything while the listing is ambiguous.
## Actions and required information
Support these v1 actions:
- **Ready:** move the whole item folder from Building to Ready. The seller's instruction to mark it Ready is confirmation that the draft is ready.
- **Posted:** require the actual posted price and posting date, write them to `posted_price` and `posted_date`, and move the whole item folder from Building or Ready to Posted.
- **Price change:** require the new current posted price, replace `posted_price`, preserve `posted_date`, and keep the listing in Posted. V1 does not preserve price history.
- **Sold:** require the actual sold price and sold date, write them to `sold_price` and `sold_date`, and move the whole item folder from Posted to Sold.
- **Closed:** move the whole item folder from Building, Ready, or Posted to Closed when the seller says the listing ended without a sale. Do not populate sold properties.

Use unquoted `YYYY-MM-DD` values for dates and numeric values for prices. Resolve an explicit `today` using the seller's local date. Do not silently interpret an omitted date as today. Preserve all unrelated properties, body content, photos, and item-folder contents.

After resolving the listing, ask one compact question containing only the missing required values. Ready needs no additional data. Closed needs no additional confirmation when the current request already says that the listing ended without a sale.
## Authority and exceptions
The current request authorizes the update without another approval when it identifies one listing, states one supported action, and includes that action's required values. Posting means recording a seller-confirmed external event; this skill never posts to a marketplace.

Pause and show the current state, proposed correction, and exact write set before correcting conflicting recorded data, reopening a Sold or Closed listing, or making a lifecycle change outside the normal transitions above. Stop if a different item folder already exists at the target path.

If the listing is already in the requested lifecycle and its tracked values match, make no changes and report that it is already current. Except for an explicit Price change, if the lifecycle matches but supplied values conflict, treat the request as a correction and obtain approval before replacing them.
## Apply and verify
Update approved properties first, then move the whole item folder when the action changes lifecycle. Verify that exactly one resulting item folder exists, `Listing.md` retains unrelated content, the tracked values match the request, and the parent lifecycle folder matches the action. `Dashboard.base` updates live and must not be regenerated.

For a routine success, report only the resulting status, recorded price and date values when applicable, exact resulting folder path, and one useful next action when one exists. Sold and Closed need no invented next action. Never post externally, contact buyers, accept an offer, or create another listing.
