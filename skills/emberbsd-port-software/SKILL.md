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

1. Find the shared recipe, patch set, and affected consumers.
2. Reproduce the issue through the real build or runtime path. Validate one pilot.
3. Fix the owning source and add a causal regression for behavior changes.
4. Build and test the affected dependency closure against independent results.
5. Check installed consumers and package lifecycle operations.
6. Prepare a focused change for review and authorized publication.

Select versionless `PKGPATH` roots through the shared Ports graph. Read [package scope](references/package-scope.md).

Cross-build on host; run target programs on VM or board.
Use SDK-selected capacity for parallelism.
Select native and target Clang/LLVM separately. Select GCC only for an explicit platform requirement.
For compilation, reject build tools outside the selected prefix. Repair missing tools in SDK or Ports.
For runtime failures, read [runtime checks](references/runtime-checks.md).
For known failures, read the matching [compatibility case](references/compatibility-cases.md).

Use `emberbsd-build-kernel` for kernel compiler preparation.
Use `emberbsd-personal-ports` for a personal application patch.
Use `emberbsd-contribute` or the [public contribution procedure](https://github.com/oxtech-ember/EmberBSD/blob/main/CONTRIBUTING.md) for authorized publication.
