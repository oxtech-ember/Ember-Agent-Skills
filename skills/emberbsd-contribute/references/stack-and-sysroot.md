# Stack and sysroot rules

Build one current package stack with shared objects and packages for each target ABI.
Keep incompatible ABIs in separate build roots.
Share the current package set and matching acceptance across devices of the same target ABI.
Update a device to the current stack before testing it.

Maintain one current sysroot per target ABI.
Build a replacement alongside it when packages or metadata become stale.
Replace the old sysroot only after the new one passes acceptance.
Reuse stack acceptance when its [input key](https://github.com/oxtech-ember/EmberBSD-SDK/blob/main/docs/input-keys.md) matches.
Otherwise, repeat the affected stack checks.
Check the kernel, DTB, display, GPU driver, radio, and firmware integration on each device.
Shared SAE acceptance does not validate another radio chip.
Split runtime and development packages; install only runtime packages on devices.
Make builds work on case-insensitive file systems.
A failure on such a file system is a recipe defect; fix the recipe.
