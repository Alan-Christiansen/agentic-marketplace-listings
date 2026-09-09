# Agentic Marketplace Listings Plugin
Shared ChatGPT/Codex and Claude Cowork skills for creating and managing Facebook Marketplace and eBay listing records in an Obsidian workspace with a live Base dashboard.
## Included skills
- `setup` creates or safely updates the Obsidian workspace.
- `new-listing` creates the listing folder and intake record, pauses for photo export, then prepares the listing after the seller confirms the photos are ready.
- `update-listing` updates lifecycle state and posted or sold details for one existing listing.

The photo pause is the default for every new listing. A seller who will not use photos can say so to proceed directly to preparation.

The skills share one Obsidian workspace model. Each platform keeps its seller-owned profile, guidance, and listing template together under `Platforms/`; eBay adds nested category guidance and templates where its listing fields diverge.
## Installation
The repository contains separate marketplace and manifest files for ChatGPT/Codex and Claude Cowork. Both hosts load the same skills and bundled workspace assets from this plugin directory. See the repository [README](../../README.md) for installation instructions.
## Current boundary
V1 supports setup, new listing preparation, and the Ready, Posted, Sold, and Closed lifecycle. It does not post externally, contact buyers, accept offers, preserve price history, or perform bookkeeping.
