---
name: emberbsd-prebuild-sdk
description: Use when you prepare a Prebuild SDK workspace or build an EmberBSD sysroot with GCC16.
---

# Prepare a Prebuild SDK

Read the [workspace workflow](references/workflow.md).
Read the command help in the selected EmberBSD-SDK source.
Use the bundled [SDK launcher](scripts/sdk.py) to run these commands.
Select the SDK source with `--sdk-source`.

1. Identify the build host and target architecture.
2. Inspect the shared workspace and its declared target.
3. For a new workspace, use `create` with `--target`.
4. For an existing target workspace, use `--adopt` with the same target.
5. Select SDK cross GCC16 and SDK native GCC16 separately.
6. Select the matching EmberBSD runtime inputs.
7. Before a sysroot build, examine its `--plan` output.
8. Before object reuse, check the recorded source, compiler, configuration and ABI.
9. Keep native generators separate from target files.
10. Record layout, build, package and target execution results separately.

An empty workspace does not prove that a compiler or sysroot works.
Reject system build tools, including native compiler fallbacks.
Before SDK distribution, check the matching packages and relocated files.
Host and target platforms are independent inputs.
Use one workspace for each target architecture.
An alias name does not establish the target.
An old layout with an unknown target needs explicit migration before a sysroot build.
For a Windows host, use the documented build environment.
Identify each untested host and target.
Shared Python modules and build logic belong to EmberBSD-SDK.

Use `emberbsd-build-kernel` for kernel-only compiler work.
Use `emberbsd-port-software` for shared dependency recipes.
Reuse current Ports recipes and patches instead of maintaining copies inside the SDK workspace.
Use `emberbsd-develop-app` for application code.
The public SDK procedure does not require these skills.
