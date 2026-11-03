---
name: emberbsd-prebuild-sdk
description: Use when you install SDK components, prepare a Prebuild SDK workspace, or build an EmberBSD sysroot.
---

# Prepare a Prebuild SDK

Read [binary component installation](references/binary-components.md) first.
For source builds, read the [workspace workflow](references/workflow.md).
Read the selected SDK command's help before execution.

1. Identify the build host and requested target architecture.
2. Select the required native tools, target ABI, compiler, and runtime.
3. Reuse compatible installed components, then obtain signed binaries from the SDK's current catalog.
4. Build unavailable components through their common Ports or OS producers.
5. For source work, inspect the workspace and the sysroot builder's `--plan`.
6. Reuse objects only when their [input key](https://github.com/oxtech-ember/EmberBSD-SDK/blob/main/docs/input-keys.md) matches.

Build only the target sysroot required for the task. Do not build every target or package group by default.
Reuse a compatible native prefix and sysroot. Kernel-only work uses `emberbsd-build-kernel` and needs no application sysroot.
An empty workspace does not prove that its compiler or sysroot works.
SDK build logic and shared Python modules belong to EmberBSD-SDK.

Reject build tools outside the selected prefix. Do not add checks that reread or rehash inputs already identified by Git or an input key.
Keep native generators separate from target files. Report host and target checks separately.

Use `emberbsd-build-kernel` for kernel-only compiler work.
Use `emberbsd-port-software` for shared dependency recipes.
Use `emberbsd-develop-app` for application code.
