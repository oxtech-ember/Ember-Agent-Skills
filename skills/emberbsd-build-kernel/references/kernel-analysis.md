# Kernel source and memory checks

Run Cppcheck on changed C/C++ kernel sources and their executable contract tests.
Valgrind cannot check a running kernel directly.
Use user-space tests of actual kernel source for applicable memory checks.
Do not describe those tests as complete kernel or hardware validation.
Use actual target headers, macros, ABI, and compile options, preferably from a compilation database.
Add Clang Static Analyzer; use GCC `-fanalyzer` only for explicit GCC profiles.
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
