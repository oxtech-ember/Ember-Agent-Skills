---
name: emberbsd-prebuild-sdk
description: Use when you prepare a Prebuild SDK workspace or build an EmberBSD sysroot.
---

# Prepare a Prebuild SDK

Read the [workspace workflow](references/workflow.md).
Read command help in the selected SDK source.
Use the bundled [SDK launcher](scripts/sdk.py) to run these commands.
Select the SDK source with `--sdk-source`.

1. Identify the build host and target architecture.
2. Inspect the shared workspace and its declared target.
3. For a new workspace, use `create` with `--target`.
4. For an existing target workspace, use `--adopt` with the same target.
5. Select native and target Clang/LLVM separately, or an explicit GCC platform profile.
6. Select the matching EmberBSD runtime inputs.
7. Before a sysroot build, examine its `--plan` output.
8. Reuse objects only by their [input key](https://github.com/oxtech-ember/EmberBSD-SDK/blob/main/docs/input-keys.md).
9. Keep native generators separate from target files.
10. Record layout, build, package and target execution results separately.

Do not add checks that reread or rehash inputs that a git hash or input key already identifies.
An empty workspace does not prove that a compiler or sysroot works.
For compilation, reject build tools outside the selected prefix.
Distribute packages and relocated files of the same input key.
Host and target platforms are independent inputs.
Use one workspace for each target architecture.
An alias name does not establish the target.
An old layout with an unknown target needs explicit migration before a sysroot build.
Identify each untested host and target.
Shared Python modules and build logic belong to EmberBSD-SDK.

Use `emberbsd-build-kernel` for kernel-only compiler work.
Use `emberbsd-port-software` for shared dependency recipes.
Reuse current Ports recipes and patches; do not copy them into the workspace.
Use `emberbsd-develop-app` for application code.
