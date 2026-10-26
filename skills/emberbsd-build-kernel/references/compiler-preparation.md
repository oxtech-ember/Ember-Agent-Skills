# Prepare the compiler

Read the [Ports cross-build procedure](https://github.com/oxtech-ember/EmberBSD-Ports/blob/main/profiles/development-toolchain/cross/README.md).
Use its original archive URL and SHA256.
Verify the selected Ports and pkgsrc revisions.
Use current Ports recipes for compiler prerequisites, transitive dependencies, and host tools.
Follow the [shared dependency contract](https://github.com/oxtech-ember/EmberBSD-Ports/blob/main/docs/update-ports.md) when updating them.
Investigate a hash mismatch before extraction.

Set `ports`, `pkgsrc`, `gcc_archive`, `tools`, and `work` to absolute paths.
Acquire `host-pkg-g16` through the [SDK tool selection procedure](https://github.com/oxtech-ember/EmberBSD-SDK/blob/main/docs/tool-selection.md).
Set `host_cc`, `host_cxx`, and `sdk_sh` to absolute paths in that native set.
Check native GCC16 versions, host CPU compatibility, and resolved paths, including symlinks.
Reject external host build-tool fallbacks.
Host system ABI headers and libraries are allowed for native tools only.
Use paths without whitespace, as the recipe requires.
The `tools` directory must contain fork-built host tools and target binutils.
Use a new compiler work directory.
Set `jobs` from available CPU, RAM, and disk capacity.

Use the selected Ports revision's `profiles/development-toolchain/cross/build.py` interface.
Run it with Python from the selected native prefix.
Pass `--kernel` and the explicit `--sdk-source` checkout.
Set `HOST_CC` and `HOST_CXX` to the selected native compiler paths.
Prepare the pkgsrc export and other inputs through the owning procedure.
Use its current argument order instead of an older copied shell command.
After preparation, check the cross GCC16 version, target triplet, and installed tool paths.


The export command requires a nonexistent destination.
Compiler selectors do not select every nested tool.
Inspect the producer's actual plan, configuration, and commands under the SDK tool selection policy.
Omit it only for a verified export from the selected revisions.
Reuse host prerequisites from `host-pkg-g16` through the recipe's current interface.
Keep source hashes, patches, math repairs, and executable regressions in Ports.
Submit tested shared repairs through the [contribution procedure](https://github.com/oxtech-ember/EmberBSD/blob/main/CONTRIBUTING.md) when publication is authorized.
Without publication permission, present the tested patch before asking.
Respect a refusal and report the repair as unsubmitted.
Do not copy a compiler workaround into skills.
The installed split-DWARF check verifies the driver's target tool lookup.
Keep compiler versions, triplets, and relevant test results.
