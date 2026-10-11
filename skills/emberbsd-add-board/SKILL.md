---
name: emberbsd-add-board
description: Use when adding an EmberBSD board or checking its kernel, boot, device-tree, and physical hardware support.
---

# Add a board

Read `README.ember.md` and `ember/boards/adding-a-board.md` in the OS repository.
Read [board evidence](references/board-evidence.md).

1. Record the exact board model, revision, firmware, and boot path.
2. Compare the closest platform with vendor wiring and interface documents.
3. Integrate kernel, drivers, DTS/ACPI, build outputs, and boot selection.
4. Run common regressions and available device checks.
5. Add a board page and a short catalog entry.
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
