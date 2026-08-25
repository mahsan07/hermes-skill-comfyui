# Test Plan

This package is documentation-first. Validate it with representative prompts and disposable fixtures.

## Required checks

1. Trigger test: confirm the skill activates for the intended request.
2. Boundary test: confirm it refuses or pauses before unauthorized side effects.
3. Failure test: provide incomplete or invalid input and verify a clear failure.
4. Privacy test: scan generated output for credentials, private endpoints, and personal data.
5. Reproducibility test: run the example twice and compare the resulting claims or artifacts.

Record command output, screenshots, or artifacts in the pull request rather than embedding sensitive data here.
