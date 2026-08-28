# Task-Adaptive Harness Contract

## Purpose

This package expresses **ComfyUI** as a typed, task-adaptive agent harness. Its concrete capability remains: Generate images, video, and audio with ComfyUI using reproducible workflows and parameter injection. The harness contract makes memory, planning, action, capability selection, failure handling, and verification explicit.

This design is informed by the four-module factorization described in *JIT-Agent: Scaling Harness Intelligence via Just-in-Time Harness Evolution* (arXiv:2608.25593). It is an independent reference implementation of the interface pattern; it does not reproduce the paper's trained model, datasets, or reported benchmark results.

## Skill-specific module mapping

| Module | Strategy | Responsibility in ComfyUI |
| --- | --- | --- |
| Memory | `entity_relationship_memory` | Retain prompt and source assets plus decisions, observations, and verification evidence needed to resume safely. |
| Planning | `dependency_and_path_traversal` | Transform model and sampler nodes into the ordered, bounded stages defined by this skill. |
| Capability | `task_conditioned_minimum_capability_set` | Expose only the production and rendering capabilities needed for the requested artifact and format. |
| Action | `brief_generate_render_inspect_export` | Advance the workflow through conditioning graph while preserving stop conditions and user authority. |

The dependency order is **Memory -> Planning -> Capability -> Action**. The action loop emits either a bounded operation or a terminal result, while the event history remains available for verification and repair.

## Operational stages

1. Choose a compatible workflow and models
2. Inject prompts seeds and dimensions
3. Wire loaders conditioning sampler and decoder
4. Queue the graph on the ComfyUI runtime
5. Track node progress and failures
6. Inspect metadata and rendered media

## Failure and repair behavior

- Schema or interface failures may be repaired at most twice.
- Permission failures stop immediately without retry or escalation.
- Consequential operations require preview and authorization when applicable.
- Verification failures produce an incomplete receipt rather than a success claim.
- A repaired plan must pass the same validation gates as the original.

## Evidence and measurements

Expected skill-specific evidence:

- `Checkpoint loader`
- `Positive prompt`
- `KSampler`
- `VAE decode`

Candidate adapters should also record task success, verification-pass rate, tool-error rate, repair count, latency, and estimated cost. These fields support controlled comparisons between a fixed general harness and a task-adaptive harness without attributing another project's results to this repository.

## Run the executable contract

```bash
python3 scripts/validate_harness.py
python3 scripts/run_harness.py examples/task.json
python3 -m unittest discover -s tests -p 'test_*.py'
```

The runner is deliberately side-effect free. It demonstrates validated module selection and produces a deterministic dry-run receipt. Connecting a real API, filesystem, model, browser, or creative runtime requires a separately reviewed adapter.

## Visual model

The existing [skill-specific system map](../assets/system-map.svg) shows the actual components and artifacts for this capability. It should be read together with the typed [manifest](../harness/manifest.json), which defines executable boundaries and evidence requirements.

## Reference

- Guibin Zhang et al., *JIT-Agent: Scaling Harness Intelligence via Just-in-Time Harness Evolution*, arXiv:2608.25593, 2026: https://arxiv.org/abs/2608.25593
