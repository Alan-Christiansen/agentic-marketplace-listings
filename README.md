# Agentic Marketplace Listings
Agentic Marketplace Listings is an Obsidian-first system for preparing and tracking items sold through Facebook Marketplace or eBay. Listings remain ordinary Markdown notes, while an Obsidian Base provides a live dashboard without creating a second data store.
## Current scope
The Codex plugin provides three skills:
- `AML: setup` creates or safely updates an Obsidian selling workspace.
- `AML: new-listing` creates a listing folder and intake record, pauses for photo export, then prepares the listing after the seller confirms the photos are ready.
- `AML: update-listing` moves an existing listing through its lifecycle and records posted or sold details.

The new-listing workflow pauses for photos by default. When a listing will have no photos, the seller can say so and continue directly to preparation.

Each listing belongs to one platform, begins from the matching platform or category template, and moves through human-visible lifecycle folders: Building, Ready, Posted, Sold, and Closed. V1 tracks posted price and sold price; it does not include cross-posting, fees, shipping costs, net proceeds, buyer messaging, or autonomous posting.
## Repository layout
- `.agents/plugins/marketplace.json` — repository-local Spectra Studio marketplace for Codex.
- `plugins/agentic-marketplace-listings/` — plugin manifest, skills, and Obsidian workspace assets.
- `docs/architecture.md` — workspace structure, ownership boundaries, and design decisions.

The repository is the canonical source for reusable engine files. Seller profiles, listings, photos, and sale records live only in each installed workspace.
## Install from GitHub
Add the repository as a Codex marketplace, then install the plugin:
```sh
codex plugin marketplace add Alan-Christiansen/agentic-marketplace-listings --ref main
codex plugin add agentic-marketplace-listings@agentic-marketplace-listings
```
Restart the ChatGPT desktop app and begin in a new task so the installed skills are loaded.
## Get updates
Refresh the Git-backed marketplace and reinstall the plugin:
```sh
codex plugin marketplace upgrade agentic-marketplace-listings
codex plugin add agentic-marketplace-listings@agentic-marketplace-listings
```
Engine-owned workspace files are changed only after an approved setup preflight. Seller profiles, listings, photos, and sale history are never overwritten.
## Development status
ChatGPT/Codex is implemented and verified first. Claude/Cowork packaging and testing remain a separate compatibility phase.
