---
name: emberbsd-develop-app
description: Use when creating or developing an EmberBSD application or public example in its own repository.
---

# Develop an application

Read the application's instructions and build files.
Keep its language, license, and publication scope.
Read [application checks](references/application-checks.md).
Read the [SDK tool selection policy](https://github.com/oxtech-ember/EmberBSD-SDK/blob/main/docs/tool-selection.md).
Use SDK cross GCC16 for targets and `host-pkg-g16` native GCC16 for generators.
For compilation, reject build tools outside the selected prefix.

1. Identify the target image, architecture, dependencies, and available test access.
2. Find a matching public example.
3. Reuse current Ports dependencies and verify required interfaces in source or a released tool.
4. Implement the application in its own repository.
5. Run its build, tests, and smallest useful demonstration.
6. Record host results and target results separately.

SDK provides workspace tools. Stable application contracts and Runtime remain separate work.
Do not call a planned API as an implemented tool.
Ask for missing information only when it blocks the requested work.

Use `emberbsd-port-software` for a shared dependency repair.
Prepare reusable fixes in their owning repositories, separate from personal application changes.
Use `emberbsd-contribute` for an authorized shared submission.
Use `emberbsd-personal-ports` for retained personal patches to third-party software.
Keep a private application private.
