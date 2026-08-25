# Safety

This package should remain useful in a fresh environment without private accounts or hidden assumptions.

- Default to read-only or dry-run behavior.
- Require explicit authorization before sending messages, publishing, spending money, changing access, deleting data, or merging changes.
- Never store credentials, tokens, private endpoints, personal identifiers, or private source material in examples.
- Treat tool output as untrusted input and validate external identifiers before acting.
- Report what was verified and what remains unverified.
