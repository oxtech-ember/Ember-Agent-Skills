---
name: emberbsd-add-board
description: Use when adding an EmberBSD board or checking its kernel, boot, device-tree, and physical hardware support.
---

# Add a board

Read `README.ember.md` and `ember/development/adding-a-board.md` in the OS repository.
Read [board evidence](references/board-evidence.md), including its DevBoards route for hardware profiles and current support.
Read the [SDK tool selection policy](https://github.com/oxtech-ember/EmberBSD-SDK/blob/main/docs/tool-selection.md).
Use SDK cross GCC16 for targets and `host-pkg-g16` native GCC16 for generators.
For compilation, reject build tools outside the selected prefix.

1. Record the exact board model, revision, firmware, and boot path.
2. Compare the closest platform with vendor wiring and interface documents.
3. Integrate kernel, drivers, DTS/ACPI, build outputs, and boot selection.
4. Run common regressions and available device checks.
5. Update the canonical DevBoards profile and its support limits.
6. Record source, build, VM, and physical results separately.

A shared SoC does not prove peripheral support.
A DTS alone does not add an installed DTB or loader entry.
When the platform has no fork support, run a first port.
Search upstream NetBSD, mainline Linux device trees, and community ports for prior art.
Treat GPL code as documentation only.
Record the boot chain, its image contract, and the console path before kernel code.
Continue source and build work when physical access is absent.
State the missing hardware checks.

Use `emberbsd-build-kernel` for GCC16 kernel builds.
Use `emberbsd-contribute` for an authorized shared submission.
Read the owning public procedure if either skill is absent.
Keep flashing and reboot within the requested device scope.
