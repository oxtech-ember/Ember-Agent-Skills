---
name: emberbsd-prebuild-sdk
description: Use when you prepare a Prebuild SDK workspace or build an EmberBSD sysroot.
---

# Prepare a Prebuild SDK

Read the [workspace workflow](references/workflow.md).
Read command help in the selected SDK source.
Use the bundled [SDK launcher](scripts/sdk.py) and select the source with `--sdk-source`.

1. Identify the build host and requested target architecture.
2. Inspect the workspace. Create or adopt one with the matching target.
3. Select the required native tools, target ABI, compiler, and runtime.
4. Inspect the sysroot builder's `--plan` before a new build.
5. Reuse objects only when their [input key](https://github.com/oxtech-ember/EmberBSD-SDK/blob/main/docs/input-keys.md) matches.

Build only the target sysroot required for the task. Do not build every target or package group by default.
Reuse a compatible native prefix and sysroot. Kernel-only work uses `emberbsd-build-kernel` and needs no application sysroot.
An empty workspace does not prove that its compiler or sysroot works.
SDK build logic and shared Python modules belong to EmberBSD-SDK.

Reject build tools outside the selected prefix. Do not add checks that reread or rehash inputs already identified by Git or an input key.
Keep native generators separate from target files. Report host and target checks separately.

Use `emberbsd-build-kernel` for kernel-only compiler work.
Use `emberbsd-port-software` for shared dependency recipes.
Use `emberbsd-develop-app` for application code.
