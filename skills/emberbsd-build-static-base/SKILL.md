---
name: emberbsd-build-static-base
description: Use when building or checking a statically linked EmberBSD base set for an appliance or recovery image.
---

# Build a static base set

Read `README.ember.md` and `ember/tools/docs/aarch64-base-update.md` in the OS repository.
Read [static build inputs](references/static-inputs.md).
Read [archive checks](references/archive-checks.md).
Read the [SDK tool selection policy](https://github.com/oxtech-ember/EmberBSD-SDK/blob/main/docs/tool-selection.md).
Use SDK cross GCC16 for targets and `host-pkg-g16` native GCC16 for generators.
For compilation, reject build tools outside the selected prefix.

1. Select a complete target compiler and runtime.
2. Build complete host tools with `host-pkg-g16` native GCC16.
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
