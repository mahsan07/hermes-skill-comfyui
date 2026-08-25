<p align="center">
  <img src="assets/overview.svg" alt="Visual overview of ComfyUI" width="100%">
</p>

# ComfyUI

> Generate images, video, and audio with ComfyUI using reproducible workflows and parameter injection.

This repository packages a single, reusable Hermes skill as a documentation-first public reference. It explains the problem, operating contract, safety boundaries, expected evidence, and example usage without claiming a bundled runtime that is not present.

## Why this exists

Creative requests often lose their intent between the initial brief, generation, export, and final quality check. **ComfyUI** turns that work into an explicit sequence with visible inputs, outputs, review points, and completion evidence.

## Why the repository has this name

The shared `hermes-skill-` prefix identifies this as a portable Hermes workflow package. `comfyui` names the capability directly—comfyui—so the repository remains searchable and understandable outside the original AI-OS workspace. The public title is **ComfyUI**.

## At a glance

| Question | Answer |
| --- | --- |
| What is it? | Creative production workflow packaged as a reusable Hermes `SKILL.md`. |
| What does it do? | Generate images, video, and audio with ComfyUI using reproducible workflows and parameter injection. |
| Who is it for? | Builders, operators, and reviewers who want a repeatable, inspectable workflow. |
| What is delivered? | A skill contract, examples, safety guidance, release checks, and rendered SVG diagrams. |
| Runtime status | Documentation-first reference package; connect it to the tools available in your own environment. |

## How it works

<p align="center">
  <img src="assets/workflow.svg" alt="Step-by-step workflow for ComfyUI" width="760">
</p>

1. Translate the request into a bounded creative brief
2. Inspect supplied assets and usage constraints
3. Choose the appropriate format and production path
4. Create a first reviewable artifact
5. Check legibility, fidelity, and export behavior
6. Deliver the artifact with revision guidance

See [How it works](docs/HOW-IT-WORKS.md) for the detailed walkthrough, decision points, and verification checklist.

## Inputs

- A clear brief, audience, format, and visual or narrative constraints
- Source assets or references the user is allowed to use
- Export requirements and acceptance criteria

## Outputs

- A reviewable visual, media, or design artifact
- The parameters or source needed to revise it
- Validation notes for format, readability, and fidelity

## Example request

> Using original or licensed sample material, generate images, video, and audio with ComfyUI using reproducible workflows and parameter injection. Return the result, the evidence used to verify it, and any limitations or actions that still require approval.

More scenarios and expected results are in [Examples](docs/EXAMPLES.md).

## Safety and trust model

<p align="center">
  <img src="assets/safety-boundary.svg" alt="Safety and approval boundaries for ComfyUI" width="900">
</p>

This workflow may create or change artifacts, so consequential actions require a preview and explicit authorization. It must stop when ownership, authorization, target state, or publication safety is ambiguous. Never place credentials, private endpoints, personal data, or environment-specific secrets in the skill package or its evidence.

Read [SAFETY.md](SAFETY.md) and [SECURITY.md](SECURITY.md) before connecting the workflow to real accounts, devices, repositories, or production data.

## What this repository does not claim

- It does not grant rights to third-party assets or replace a final human creative review.
- It is not a hosted service, executable application, or vendor endorsement.
- It does not include credentials, private infrastructure, or the original personal AI-OS configuration.
- A successful example does not prove production readiness for every environment.

## Repository map

| Path | Purpose |
| --- | --- |
| `SKILL.md` | Concise trigger conditions and operating workflow used by an agent. |
| `docs/PRODUCT.md` | Problem framing, audience, boundaries, and readiness model. |
| `docs/HOW-IT-WORKS.md` | Expanded walkthrough with diagrams and verification points. |
| `docs/EXAMPLES.md` | Realistic safe, review-only, and stop-condition scenarios. |
| `docs/RELEASE.md` | Checks to complete before publishing a revision. |
| `assets/*.svg` | Accessible, GitHub-rendered visual explanations. |
| `tests/README.md` | Manual contract and package validation guidance. |
| `SAFETY.md` / `SECURITY.md` | Operational and disclosure boundaries. |

## Use this package

1. Read `SKILL.md` and confirm its trigger matches your task.
2. Copy the package into the skill location supported by your agent environment, or use it as a reference when authoring an equivalent workflow.
3. Replace tool assumptions with the tools actually available to you; do not add secrets to the repository.
4. Run the smallest safe example from `docs/EXAMPLES.md`.
5. Record verification evidence and review any consequential action before widening scope.

## Contributing

Improvements are welcome when they preserve narrow scope, honest capability claims, safe defaults, and reproducible verification. See [CONTRIBUTING.md](CONTRIBUTING.md).
