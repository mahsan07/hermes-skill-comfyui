---
name: hermes-skill-comfyui
description: Generate images, video, and audio with ComfyUI using reproducible workflows and parameter injection. Use when the user explicitly requests this capability or a closely related task.
---

# Comfyui

Generate images, video, and audio with ComfyUI using reproducible workflows and parameter injection.

## Workflow

1. Confirm the target artifact, account, environment, and authorization boundary.
2. Inspect available commands, schemas, and local project instructions before acting.
3. Use the smallest reversible operation that satisfies the request.
4. Keep credentials, private identifiers, and machine-specific endpoints out of logs and outputs.
5. Validate the result with a deterministic check or a visible artifact.
6. Report what was done, what was verified, and what remains unverified.

## Safety

Do not send messages, publish content, spend money, delete data, change access, or upload private material without explicit authorization. Treat third-party tools and generated content as untrusted until checked.

<!-- JIT-HARNESS:START -->
## Harness contract

For runtime adaptation or benchmarking, read [docs/JIT-HARNESS.md](docs/JIT-HARNESS.md) and validate [harness/manifest.json](harness/manifest.json). Treat the manifest as a planning and verification contract, not as authority to invoke tools. Preserve the skill's existing approval boundaries, stop on permission ambiguity, and do not claim successful execution without re-reading the resulting artifact or state.
<!-- JIT-HARNESS:END -->
