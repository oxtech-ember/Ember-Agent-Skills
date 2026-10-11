# Application checks

Set `app`, `examples`, `sdk`, and `runtime` to actual checkouts.
Inspect their tracked files and interface definitions.

```sh
git -C "$app" status --short
rg --files "$app" "$examples" | rg '(^|/)(README[^/]*|Makefile|CMakeLists\.txt|meson\.build|.*test[^/]*)$'
rg -n "$required_interface" "$sdk" "$runtime" "$examples"
```

For `rg`, status 1 means no match.
Status 2 means a failed search.
Check each exit status before the next dependent command.

Read the matching example's README and build definition.
Use its documented commands and dependencies.
An application change usually needs no OS rebuild.
Check the selected target's actual compiler and loaded runtime.
Record expected output and one useful failure case.
State which checks need unavailable hardware.
Store the test receipt beside the application.

Use public fixtures in shared examples.
Make device names and configuration parameters replaceable.
Preserve source attribution.
Route OS defects to [EmberBSD](https://github.com/oxtech-ember/EmberBSD).
Route dependency recipes to [Ports](https://github.com/oxtech-ember/EmberBSD-Ports).
Route public demonstrations to [Examples](https://github.com/oxtech-ember/EmberBSD-Examples).

Verify [SDK](https://github.com/oxtech-ember/EmberBSD-SDK) and [Runtime](https://github.com/oxtech-ember/EmberBSD-Runtime) implementations before use.
Planned Wasm formats and hardware adapters supply no executable interface.
Project names do not establish an `ember` command or MCP server.
The AI plugin catalog and the proposed device application catalog serve different purposes.

## Source and memory analysis

For C/C++ changes, run Cppcheck on the affected source and test code.
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
