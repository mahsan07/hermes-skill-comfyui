# Product Definition

## What it is

Comfyui is a focused, shareable agent workflow.

## What it does

Generate images, video, and audio with ComfyUI using reproducible workflows and parameter injection. Use when the user explicitly requests this capability or a closely related task.

## Who it is for

Builders who want a repeatable workflow that can be used without knowing the original private system.

## Core workflow

1. Confirm the request, target, and authorization boundary.
2. Inspect available inputs, schemas, and project instructions.
3. Execute the smallest reversible workflow.
4. Validate the result with a deterministic check or visible artifact.
5. Report evidence, assumptions, and remaining uncertainty.

## MVP acceptance criteria

- The skill triggers on a clear class of requests.
- The workflow works with local or disposable inputs.
- Examples contain no secrets or private identifiers.
- Failure and approval boundaries are documented.
- A reviewer can reproduce the validation steps.
