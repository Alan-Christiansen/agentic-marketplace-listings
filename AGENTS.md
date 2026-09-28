# Agent Instructions
Build the smallest mechanism that removes demonstrated seller friction. Keep ordinary operation understandable without AI, and never invent item facts, condition, stamp grading, prices, or platform requirements.
## Sources of truth
- Plugin sources, portable workspace assets, tests, validation, releases, and implementation documentation live in this repository.
- Project purpose, lifecycle, PM state, accepted project decisions, and handoffs live in the developer's human-owned project record outside this public repository.
- Conversations and provider memory are supporting context only.
## Working rules
- Read `README.md` and, when it is available in the local development environment, the relevant human-owned project record before meaningful implementation work.
- Read the current Technical Brief before proposing product, plugin, data, or release architecture changes.
- Preserve one provider-neutral skill source and keep host-specific manifests and adapters thin.
- Validate Codex and Claude packaging, installation, and invocation independently.
- Keep engine-owned files separate from seller-owned settings, listings, photos, and historical records.
- Keep public artifacts free of secrets, private seller data, and required assumptions about one user's vault layout.
- Preserve unrelated changes and verify work in proportion to risk.
- Propose major scope, dependency, architecture, lifecycle, external-service, or destructive changes before acting.
- Do not infer permission to create remotes, commit, push, publish, deploy, purchase, message, or install dependencies.
- End meaningful work with a concise handoff in the canonical project record.
