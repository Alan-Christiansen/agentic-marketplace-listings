# Contributing
Thank you for helping improve Agentic Marketplace Listings.
## Before starting
Use [GitHub Issues](https://github.com/Alan-Christiansen/agentic-marketplace-listings/issues) to report a bug or suggest an improvement. Please open an issue before beginning a substantial feature, workflow change, or new platform integration so the scope and ownership boundaries can be discussed first.
## Pull requests
- Keep changes focused and preserve the plain-file Obsidian workflow.
- Keep shared behavior provider-neutral. Add host-specific files only when a tested host difference requires them.
- Never include real seller data, listing photos, credentials, or private filesystem paths.
- Do not weaken the approval boundaries around file replacement, pricing, posting, buyer communication, or destructive changes.
- Update documentation and validation when behavior or packaging changes.
## Validation
From the repository root, run:
```sh
python3 scripts/validate.py
claude plugin validate .
```

Codex plugin and skill validators should also pass before a release. Test host installation and behavior from a fresh task, using a disposable workspace rather than real seller data.
## License
By contributing, you agree that your contributions will be licensed under the repository's [MIT License](LICENSE).
