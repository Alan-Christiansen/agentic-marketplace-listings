# Agentic Marketplace Listings Plugin
Codex skills for creating and managing Facebook Marketplace and eBay listing records in an Obsidian workspace with a live Base dashboard.
## Included skills
- `$agentic-marketplace-listings:setup` (`AML: setup`) creates or safely updates the Obsidian workspace.
- `$agentic-marketplace-listings:new-listing` (`AML: new-listing`) creates the listing folder and intake record, pauses for photo export, then prepares the listing after the seller confirms the photos are ready.
- `$agentic-marketplace-listings:update-listing` (`AML: update-listing`) updates lifecycle state and posted or sold details for one existing listing.

The photo pause is the default for every new listing. A seller who will not use photos can say so to proceed directly to preparation.

The skills share one Obsidian workspace model. Each platform keeps its seller-owned profile, guidance, and listing template together under `Platforms/`; eBay adds nested category guidance and templates where its listing fields diverge.
## Installation
The repository contains a Codex marketplace at `.agents/plugins/marketplace.json`. It can be added from a local checkout during development or from `Alan-Christiansen/agentic-marketplace-listings` for independent installation and updates.
## Current boundary
V1 supports setup, new listing preparation, and the Ready, Posted, Sold, and Closed lifecycle. It does not post externally, contact buyers, accept offers, preserve price history, or perform bookkeeping. Claude/Cowork packaging remains separate from the completed Codex implementation.
