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
For physical boot, read the exact [DevBoards](https://github.com/oxtech-ember/EmberBSD-DevBoards) profile.
Locate it through the [reader guide](https://github.com/oxtech-ember/EmberBSD-DevBoards/blob/main/docs/reader-guide.md) and [catalog](https://github.com/oxtech-ember/EmberBSD-DevBoards/blob/main/catalog.json).
Check its current support limits, boot layout, and selected loader contract.
A shared SoC does not establish the image format.
Read OS builder and image contracts beside their implementation.
Apply them only to the hardware and boot layout identified by DevBoards.
QEMU `-kernel` can differ from the guest's `/netbsd` file.
Compilation alone does not prove boot or peripheral support.
Keep firmware and hardware checks within the requested device scope.

For linked applications, read the Ports recipe's application mode.
It requires target libc, startup objects, headers, and the matching GCC16 runtime.
Run its `compile-tests.sh` and target runner.
Preserve sysroot provenance and relative symlinks.
Do not mix host libraries with target libraries.

## Source and memory analysis

Run Cppcheck on changed C/C++ kernel sources and their executable contract tests.
Valgrind cannot check a running kernel directly.
Use user-space tests of actual kernel source for applicable memory checks.
Do not describe those tests as complete kernel or hardware validation.
Use actual target headers, macros, ABI, and compile options, preferably from a compilation database.
Add GCC `-fanalyzer` for C and Clang Static Analyzer for C/C++ where supported.
Check analyzer support in the selected compiler version.
Run executable tests with Valgrind Memcheck on a supported platform.
Enable leak and uninitialized-value checks with a nonzero error exit status.
Valgrind checks execution, not source text.
If Valgrind is unavailable, record the platform gap and applicable ASan/UBSan or kernel checks.
Do not label substitute checks as a Valgrind pass.
Fix confirmed defects with regressions.
Track unresolved inherited findings with their owner and impact.
Explain each targeted suppression; do not disable whole diagnostic categories.
Record tool versions, commands, scope, findings, and untested paths.
Static analysis and memory checks supplement runtime and hardware acceptance.

Tool references: [Cppcheck](https://cppcheck.sourceforge.io/manual.html),
[GCC analyzer](https://gcc.gnu.org/onlinedocs/gcc/Static-Analyzer-Options.html),
[Clang analyzer](https://clang.llvm.org/docs/ClangStaticAnalyzer.html),
and [Valgrind platforms](https://valgrind.org/info/platforms.html).

## Driver structure

Attach drivers through autoconf(9); declare options and dependencies in `files.*`.
Make each driver possible to disable with a configuration option.
Do not add hard dependencies between optional drivers.
Use shared helpers such as firmload(9), net80211, and DRM helpers.
Add a man page for a new driver and follow style(9).
