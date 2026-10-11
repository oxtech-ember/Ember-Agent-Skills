# Build and check the kernel

Set `os` to the source checkout.
Set `output` to an absolute directory outside the OS source tree.
Use the same selected host compilers and resource limit.

```sh
HOST_CC=gcc HOST_CXX=g++ CC=gcc NETBSD2_JOBS="$jobs" \
    EMBER_EXTERNAL_TOOLCHAIN="$work/toolchain" \
    sh "$os/ember/build-kernel.sh" "$output" EMBER64
```

Inspect the builder before selecting another architecture or configuration.
Verify cached compiler settings and the actual external prefix.
Check the real exit status and current logs.
Reject stale artifacts from a failed build.
Inspect ELF architecture, kernel configuration, modules, DTBs, and image hashes.
Keep kernel, modules, and DTBs from coherent inputs.
Run the owning portable contracts and applicable orchestration regression.
Record native contract gaps explicitly.

Identify the artifact that the loader actually selects.
QEMU `-kernel` can differ from the guest's `/netbsd` file.
Compilation alone does not prove boot or peripheral support.
Keep firmware and hardware checks within the requested device scope.

For linked applications, read the Ports recipe's application mode.
It requires target libc, startup objects, headers, and the matching GCC16 runtime.
Run its `compile-tests.sh` and target runner.
Preserve sysroot provenance and relative symlinks.
Do not mix host libraries with target libraries.
