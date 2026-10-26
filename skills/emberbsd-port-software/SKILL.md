---
name: emberbsd-port-software
description: Use when adding, modernizing, or repairing shared EmberBSD Ports recipes, dependencies, compiler runtimes, or portability patches.
---

# Port and modernize shared software

Read the Ports README and owning profile.
Read [shared dependencies and contributions](references/shared-dependencies.md).
Read [recipe checks](references/recipe-checks.md).
For version or dependency migrations, read [modernization checks](references/modernization-checks.md).
For a Ports update request, read [agent-driven updates](references/update-ports.md).

1. Find the current shared recipe, patches, and affected consumers in Ports.
2. Reproduce the failure with the real build or runtime path.
3. Validate one affected component as a pilot.
4. Fix the cause in Ports or the owning upstream source.
5. Rebuild the affected dependency set with the shared toolchain.
6. Run upstream tests and local regressions against independent expected results.
7. Compare observable behavior and test that the checks detect deliberate faults.
8. Check installed consumers and package lifecycle operations.
9. Record revisions, hashes, commands, test counts, results, and gaps.
10. Prepare the shared fix for review and submit its PR when publication is authorized.

Cross-build on the development host.
Run target programs on the VM or board.
Size build parallelism from host resources, not guest RAM.

For runtime or media failures, read [runtime checks](references/runtime-checks.md).
For known failures, read the matching [compatibility case](references/compatibility-cases.md).
Reuse one current Ports version per dependency across the selected closure.
Use SDK cross GCC16 for targets and `host-pkg-g16` native GCC16 for generators.
For compilation, reject build tools outside the selected prefix.
Follow the [SDK tool policy](https://github.com/oxtech-ember/EmberBSD-SDK/blob/main/docs/tool-selection.md).
Repair missing tools in SDK/Ports; reject private wrappers and legacy stacks.

Use `emberbsd-build-kernel` for kernel compiler preparation.
Use `emberbsd-personal-ports` for a personal application patch.
Use `emberbsd-contribute` or the public contribution procedure for authorized publication.
Keep caches and binaries outside Git.
