# Prepare the compiler

Read the [SDK tool selection procedure](https://github.com/oxtech-ember/EmberBSD-SDK/blob/main/docs/tool-selection.md).
Read the [native Clang procedure](https://github.com/oxtech-ember/EmberBSD-Ports/blob/main/profiles/development-toolchain/darwin-bootstrap.md) for a Darwin host.
For an explicit GCC target, read the [GCC procedure](https://github.com/oxtech-ember/EmberBSD-Ports/blob/main/profiles/development-toolchain/cross/README.md).
Verify the selected Ports and pkgsrc revisions.
Use shared Ports recipes for compilers, prerequisites, transitive dependencies, and native tools.
Check source archive hashes before extraction.
Keep compiler patches and executable regressions in Ports.

Select Clang/LLVM by default.
Use GCC only for an explicit platform requirement.
Select host and target compiler families independently.
A host generator needs the host OS and CPU, even when its output describes another target.
Select the target triplet explicitly for Clang.
Keep native ABI headers and libraries outside target searches.

Obtain initial tools through the declared Ports bootstrap procedure.
Initial acquisition does not require a completed SDK.
For ordinary builds, check resolved tool paths, host CPU, and compiler-selected components inside the selected prefix.
Reject automatic fallback to system tools or another compiler family.
Use the current producer interface and inspect its plan before compilation.
A compiler environment variable does not select every nested tool.

Kernel-only builds use the owning producer's target inputs without an application sysroot.
Application builds additionally require target headers, libc, CRT, and the selected runtime.
Compiler choice alone does not establish C++ ABI compatibility.
Select jobs from available host CPU, memory, disk, and active builds.
Use the shared object tree and keep incompatible configurations separate.
Reuse exports and installed tools when their [input key](https://github.com/oxtech-ember/EmberBSD-SDK/blob/main/docs/input-keys.md) matches.
Do not make a new admission report for them.

Check actual command results, target objects, and relevant compiler tests.
Keep build evidence separate from boot and hardware evidence.
Submit authorized shared fixes through the [contribution procedure](https://github.com/oxtech-ember/EmberBSD/blob/main/CONTRIBUTING.md).
Without publication permission, prepare the tested patch before asking.
Respect a refusal and report the repair as unsubmitted.
