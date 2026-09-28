---
name: marketplace-update-listing
description: Update one existing Agentic Marketplace Listings record through Ready, Posted, price-change, Sold, or Closed lifecycle actions. Use when the seller wants to change the state or tracked posted or sold details of a known listing. Do not use for external posting, buyer communication, bookkeeping, or an ambiguous listing.
---
# Marketplace: Update Listing
Record one lifecycle change for one existing listing, in the same turn when the request is complete. Follow the plugin's [operating policy](../../references/operating-policy.md).
## Resolve
Confirm the workspace is initialized, resolve exactly one listing, and read only its `Listing.md`. Stop if a different item folder already occupies the target path.
## Actions
| Action | From | To | Requires | Writes |
| --- | --- | --- | --- | --- |
| Ready | Building | Ready | Nothing | Nothing |
| Posted | Building, Ready | Posted | Posted price and date | `posted_price`, `posted_date` |
| Price change | Posted | Posted | New price | `posted_price`; keep `posted_date` |
| Sold | Posted | Sold | Sold price and date | `sold_price`, `sold_date` |
| Closed | Building, Ready, Posted | Closed | Listing ended without a sale | Nothing; never sold fields |

If required values are missing, ask one question containing only those values. "Posted" records an event the seller reports; this skill never posts to a marketplace.
## Approval
A request that names one listing, one action above, and its required values is the approval. Apply it without asking again.

Pause and show the current state, the proposed change, and the exact write set before correcting recorded values, reopening a Sold or Closed listing, or making a transition not in the table. If the listing is already in the requested state with matching values, change nothing and say so.
## Apply
Write the properties, then move the whole item folder when the lifecycle changes. Preserve all other properties, body content, and photos. Report the resulting status, any recorded values, and the folder path. Add a next step only when one exists.
