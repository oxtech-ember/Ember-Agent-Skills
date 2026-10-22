# Recipe checks

Set `ports` to the owning checkout.
Inspect its pinned package sources before writing another recipe.

```sh
git -C "$ports" submodule status
rg --files "$ports/profiles" "$ports/probes" | rg '(README\.md|sources\.tsv|build\.sh|test.*\.sh)$'
rg -n "$dependency" "$ports/profiles" "$ports/probes"
```

Select current stable upstream or a justified supported LTS release.
Record release date, source revision, original URL, SHA256, and patch authorship.
Verify archives before extraction.
Investigate changed hashes instead of replacing expected values without evidence.
Preserve licenses and required private-fork backends.
Use ordinary pkgsrc recipes, staging, and package tools.

Check CPU, RAM, and disk capacity before setting job limits.
Coordinate access to a shared build host.
Use new outputs after compiler or configuration changes.
Keep actual exit statuses.
A failed build, skipped test, or success stub establishes no pass.

| Change | Required evidence |
| --- | --- |
| Compiler | Atomics, threads, TLS, DSO exceptions, loaded runtime |
| Ruby | Package tests and a loaded native extension |
| Go | Module tests and required cgo paths |
| TinyGo | Actual Wasm/WASI execution or MCU compilation |
| Package | Build, tests, staged install, remove, reinstall |
| Library | Installed consumers, expected result, invalid input, lifecycle |
| Media | Selected backend, frames, timestamps, state, EOF, damaged input |

MCU compilation does not prove flashing or device execution.
Keep device writes within the requested scope.

## Source and memory analysis

Run Cppcheck on C/C++ sources in the pinned upstream release and the patched port.
Compare findings before and after patches with equivalent target settings.
Separate inherited findings from errors introduced by the port.
Keep reusable fixes and regression checks in Ports.
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

## One package stack

Build every package in the one shared build directory and sysroot.
Do not create package variants for one device.
Split large toolchains into runtime and development packages.
Target runtime packages must not depend on compilers, linkers, or test tools.
Rebuild in a clean work directory after a version or file-list change.
Check that each `PROVIDES` entry names a file in the package's `+CONTENTS`.
Remove stale sysroot packages; clean and rebuild the sysroot when needed.
Rebuild ABI consumers in the same change.
