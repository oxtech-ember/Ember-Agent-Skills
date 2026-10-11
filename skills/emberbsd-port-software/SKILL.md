---
name: emberbsd-port-software
description: Use when adding or repairing a shared EmberBSD Ports recipe, dependency, compiler runtime, or portability patch.
---

# Port shared software

Read the Ports AGENTS.md and owning profile.
Read [recipe checks](references/recipe-checks.md).

1. Verify the selected upstream release and pinned package sources.
2. Reproduce the failure with the real build or runtime path.
3. Fix the cause in Ports or the owning upstream source.
4. Rebuild the affected dependency set.
5. Run upstream tests and the relevant local regression.
6. Check installed consumers and package lifecycle operations.
7. Record revisions, hashes, commands, results, and remaining gaps.

For runtime or media failures, read [runtime checks](references/runtime-checks.md).
For a known compatibility case, read only the matching [case reference](references/compatibility-cases.md).
Historical versions are evidence, not permanent version requirements.
Retest a workaround when its upstream condition changes.

Use `emberbsd-build-kernel` for kernel compiler preparation.
Use `emberbsd-personal-ports` for a personal application patch.
Use `emberbsd-contribute` when shared publication is authorized.
Keep caches and binaries outside Git.
