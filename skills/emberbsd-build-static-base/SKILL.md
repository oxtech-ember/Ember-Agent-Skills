---
name: emberbsd-build-static-base
description: Use when building or checking a statically linked EmberBSD base set for an appliance or recovery image.
---

# Build a static base set

Read the OS AGENTS.md and `ember/boot/aarch64-base-update.md`.
Read [static build inputs](references/static-inputs.md).
Read [archive checks](references/archive-checks.md).

1. Select a complete target compiler and runtime.
2. Build complete host tools.
3. Use separate static object and destination directories.
4. Apply the owning reduced base profile and static link settings.
5. Fix missing generation dependencies in OS make rules.
6. Check the archive and candidate binaries before deployment.

GCC16 kernel frontends alone cannot build a complete static base runtime.
Keep normal file checks and `INSTALLSETS=base`.
Do not retry compiler crashes as a substitute for diagnosis.
Use the owning recovery procedure for an authorized deployment.
Record measured boot results instead of assuming a speed improvement.
Keep build evidence and physical acceptance separate.
