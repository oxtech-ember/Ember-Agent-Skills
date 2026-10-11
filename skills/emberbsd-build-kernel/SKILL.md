---
name: emberbsd-build-kernel
description: Use when preparing a GCC16 cross compiler or building an EmberBSD kernel without an application sysroot.
---

# Build a GCC16 kernel

Read the OS and Ports build guides.
Read [compiler preparation](references/compiler-preparation.md).
Read [kernel checks](references/kernel-checks.md).

1. Identify the host, target architecture, source revision, and available resources.
2. Verify host GCC and G++ versions and triplets.
3. Prepare the pinned Ports export and original GCC archive.
4. Build the cross compiler with the public Ports `--kernel` mode.
5. Select that prefix through `EMBER_EXTERNAL_TOOLCHAIN`.
6. Run the owning OS kernel builder.
7. Check its exit status, logs, contracts, and artifacts.

Check each exit status before the next dependent command.

Require GCC16 on both host and target for this workflow.
The OS bootstrap defaults to GCC12.5.
Do not accept an implicit GCC12 or GCC14 fallback.
Kernel mode needs no application sysroot.
A kernel compiler supplies no complete target application runtime.
Repair shared compatibility in Ports or OS.
Record build evidence separately from boot and hardware evidence.
