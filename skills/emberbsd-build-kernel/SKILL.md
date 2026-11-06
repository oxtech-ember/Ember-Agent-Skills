---
name: emberbsd-build-kernel
description: Use when preparing a target compiler or building an EmberBSD kernel without an application sysroot.
---

# Build an EmberBSD kernel

Read the OS and Ports build guides.
Read [compiler preparation](references/compiler-preparation.md).
Read [kernel checks](references/kernel-checks.md).

1. Identify the host, target architecture, source revision, and available resources.
2. Inspect installed tools and the authenticated SDK catalog and plan. Reuse compatible tools, then install matching signed binaries.
3. For missing components, follow the owning host bootstrap and prepare the pinned Ports export and compiler inputs.
4. Use the owning Ports procedure for the selected compiler family and kernel target.
5. Select the compiler family, target, and prefix through the current OS interface.
6. Run the owning OS kernel builder.
7. Check its exit status, logs, contracts, and artifacts.

Check each exit status before the next dependent command.

Select native Clang/LLVM by default, or an explicit GCC platform profile.
Build missing native tools from common Ports recipes, then build the cross SDK with them.
Initial acquisition does not require a completed SDK.
For compilation, reject build tools outside the selected prefix.
Read the [SDK tool selection policy](https://github.com/oxtech-ember/EmberBSD-SDK/blob/main/docs/tool-selection.md).
Kernel mode needs no application sysroot.
A kernel compiler supplies no complete target application runtime.
Repair shared compatibility in Ports or OS.
Record build evidence separately from boot and hardware evidence.
