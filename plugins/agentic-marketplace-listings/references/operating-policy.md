# Operating Policy
## Sources of truth
- The item folder's parent lifecycle folder is its status.
- `Listing.md` is the source of truth for item facts and listing data.
- `Dashboard.base` is a live derived view, never a second source of truth.
- `Platforms/Facebook/Seller Profile.md` and `Platforms/eBay/Seller Profile.md` control voice and recurring seller preferences; approved examples in those profiles demonstrate style only.
- Platform and category guidance and templates describe reusable requirements and record structure, not item facts.
## Item identification
When a request concerns an existing listing, resolve it from the current or explicitly linked `Listing.md`, an exact folder path, or a sufficiently distinctive human-readable item name. If more than one listing could match, show the candidates and ask which one. Do not guess from recent conversation alone when ambiguity could update the wrong item.
## Fact integrity
- Never invent identity, model, measurements, condition, defects, provenance, price, catalog information, stamp grade, or platform requirements.
- Distinguish visible evidence, seller-supplied facts, external research, and inference.
- Preserve useful unknowns. Ask only when missing information blocks an accurate or safe next step.
- Treat approved examples as prose guidance, never as evidence for the current item.
## Lifecycle and tracking
Use exactly these lifecycle folders: Building, Ready, Posted, Sold, and Closed. Moves between them are the status change. Record only the current posted price/date and sold price/date in v1. `Dashboard.base` derives time to sell when both dates exist. Do not add fees, shipping costs, net proceeds, or price-history records unless the system is deliberately expanded later.
## Photos
Working photos belong beside `Listing.md`. Originals live elsewhere. Do not create an originals/archive pipeline. Resize or compress working copies only when the seller requests it or an actual upload constraint makes it useful, and do not silently replace the supplied files.
## Authority boundaries
The agent may organize and draft within the requested workspace. It must not post externally, contact buyers, accept offers, commit to a price, delete seller data, publish, install, or perform unrelated changes without appropriate authorization.
