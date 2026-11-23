# Build and check the kernel

Set `sdk_python` to the absolute Python path in the selected native prefix.
For a Clang kernel, use an SDK build profile.
Read the [build profile procedure](https://github.com/oxtech-ember/EmberBSD-SDK/blob/main/docs/build-profile.md).
Set `client` to the client configuration and `profile` to the profile file.
Name the kernel configuration in `os.kernels` of the profile.
Select a [general-purpose configuration](https://github.com/oxtech-ember/EmberBSD/blob/main/ember/development/kernel.md#kernel-configurations) or a local trial in `build.kernel_configs`.
Run the command from the SDK checkout:

```sh
"$sdk_python" scripts/packages.py --config "$client" profile-build --profile "$profile"
```

`profile-build` runs `ember/build-kernel.sh` with the selected tools and prepared sources.
It writes the kernel to the `kernels` directory of the configured `work` directory.

The profile supports only the Clang target toolchain.
For an explicit GCC platform profile, run the OS kernel builder directly.
Set `os` to the source checkout.
Set `output` to an absolute directory outside the OS source tree.
Use the same selected host compilers and resource limit.

```sh
HOST_CC="$host_cc" HOST_CXX="$host_cxx" CC="$host_cc" NETBSD2_JOBS="$jobs" \
    EMBER_BUILD_MODE=cross NETBSD2_PYTHON="$sdk_python" \
    EMBER_EXTERNAL_TOOLCHAIN="$work/toolchain" \
    "$sdk_sh" "$os/ember/build-kernel.sh" "$output" EMBER64
```

Inspect the builder before selecting another architecture or configuration.
Verify cached compiler settings and the actual external prefix.
Verify separate host and target compiler selections in nested commands.
Reject stale caches and system-tool selection before compiling.
Check the real exit status and current logs.
Reject stale artifacts from a failed build.
Inspect ELF architecture, kernel configuration, modules, DTBs, and image hashes.
Keep kernel, modules, and DTBs from coherent inputs.
Run the owning portable contracts and applicable orchestration regression.
Record native contract gaps explicitly.

Identify the artifact that the loader actually selects.
For physical boot, read the exact [DevBoards](https://github.com/oxtech-ember/EmberBSD-DevBoards) profile.
Locate it through the [reader guide](https://github.com/oxtech-ember/EmberBSD-DevBoards/blob/main/docs/reader-guide.md) and [catalog](https://github.com/oxtech-ember/EmberBSD-DevBoards/blob/main/catalog.json).
Check its current support limits, boot layout, and selected loader contract.
A shared SoC does not establish the image format.
Read OS builder and image contracts beside their implementation.
Apply them only to the hardware and boot layout identified by DevBoards.
QEMU `-kernel` can differ from the guest's `/netbsd` file.
On a running efiboot AArch64 board, install with `ember/install-kernel.sh`; it keeps a recovery kernel.
Compilation alone does not prove boot or peripheral support.
Keep firmware and hardware checks within the requested device scope.

For linked applications, read the Ports recipe's application mode.
It requires target libc, startup objects, headers, and the matching compiler runtime.
Run its current `compile-tests.py` procedure and target runner.
Preserve sysroot provenance and relative symlinks.
Keep host libraries outside target library searches.

## Source and memory analysis

Run [kernel source and memory checks](kernel-analysis.md) for changed code.

## Driver structure

Assign protocols and policy to common owners; assign hardware and vendor interface translation to drivers.
Expose offload through common contracts and retain required device-specific backends and asynchronous transports.
When a common API is missing, extend its owner, adapt consumers, and remove duplicate policy as part of the extension.
Report capabilities and errors; enforce bounds and security at the hardware boundary.
Add the hardware adapter after common behavior is ready.
Reuse common regressions and test the hardware boundary.

Attach drivers through autoconf(9); declare options and dependencies in `files.*`.
Make each driver possible to disable with a configuration option.
Keep each optional driver usable when unrelated optional drivers are disabled.
Use shared helpers such as firmload(9), net80211, and DRM helpers.
Add a man page for a new driver and follow style(9).
