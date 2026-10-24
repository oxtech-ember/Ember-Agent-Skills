---
name: emberbsd-build-kernel
description: Use when preparing a GCC16 cross compiler or building an EmberBSD kernel without an application sysroot.
---

# Build a GCC16 kernel

Read the OS and Ports build guides.
Read [compiler preparation](references/compiler-preparation.md).
Read [kernel checks](references/kernel-checks.md).

1. Identify the host, target architecture, source revision, and available resources.
2. Verify SDK native GCC16 provenance, version, and host triplet.
3. Prepare the pinned Ports export and original GCC archive.
4. Build the cross compiler with the public Ports `--kernel` mode.
5. Verify the resulting cross compiler before selecting its prefix through `EMBER_EXTERNAL_TOOLCHAIN`.
6. Run the owning OS kernel builder.
7. Check its exit status, logs, contracts, and artifacts.

Check each exit status before the next dependent command.

Require SDK tools for bootstrap, native generators, and target compilation.
Reject system compiler and build-tool fallbacks.
Read the [SDK tool selection policy](https://github.com/oxtech-ember/EmberBSD-SDK/blob/main/docs/tool-selection.md).
Kernel mode needs no application sysroot.
A kernel compiler supplies no complete target application runtime.
Repair shared compatibility in Ports or OS.
Record build evidence separately from boot and hardware evidence.
