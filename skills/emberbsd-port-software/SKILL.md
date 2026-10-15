---
name: emberbsd-port-software
description: Use when adding, modernizing, or repairing shared EmberBSD Ports recipes, dependencies, compiler runtimes, or portability patches.
---

# Port and modernize shared software

Read the Ports README and owning profile.
Read [recipe checks](references/recipe-checks.md).
For version or dependency migrations, read [modernization checks](references/modernization-checks.md).

1. Record the supported behavior, target release, and dependency changes.
2. Reproduce the failure with the real build or runtime path.
3. Validate one affected component as a pilot.
4. Fix the cause in Ports or the owning upstream source.
5. Rebuild the affected dependency set with the shared toolchain.
6. Run upstream tests and local regressions against independent expected results.
7. Compare observable behavior and test that the checks detect deliberate faults.
8. Check installed consumers and package lifecycle operations.
9. Record revisions, hashes, commands, executed test counts, results, and remaining gaps.

Cross-build on the development host.
Run target programs on the VM or board.
Size build parallelism from host resources, not guest RAM.

For runtime or media failures, read [runtime checks](references/runtime-checks.md).
For a known compatibility case, read only the matching [case reference](references/compatibility-cases.md).
Use current standard EmberBSD tools and shared supported dependencies.
Use the common GCC16 profile.
Never install older compilers or libraries to satisfy dependency builds.
Patch incompatible consumers instead of adding parallel legacy versions.
Historical versions remain evidence.

Use `emberbsd-build-kernel` for kernel compiler preparation.
Use `emberbsd-personal-ports` for a personal application patch.
Use `emberbsd-contribute` when shared publication is authorized.
Keep caches and binaries outside Git.
