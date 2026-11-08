# Board source and memory checks

Run Cppcheck on changed C/C++ drivers, board code, and executable contract tests.
Valgrind cannot check kernel code or device DMA directly.
Use suitable user-space contracts and target kernel diagnostics.
Use actual target headers, macros, ABI, and compile options, preferably from a compilation database.
Add Clang Static Analyzer; use GCC `-fanalyzer` only for explicit GCC profiles.
Check analyzer support in the selected compiler version.
Run executable tests with Valgrind Memcheck on a supported platform.
Enable leak and uninitialized-value checks with a nonzero error exit status.
Valgrind checks execution, not source text.
If Valgrind is unavailable, record the platform gap and applicable ASan/UBSan or kernel checks.
Name each substitute check. Report any Valgrind run separately with its actual result.
Fix confirmed defects with regressions.
Track unresolved inherited findings with their owner and impact.
Keep diagnostic categories enabled. Explain each narrowly targeted suppression.
Record tool versions, commands, scope, findings, and untested paths.
Static analysis and memory checks supplement runtime and hardware acceptance.

Tool references: [Cppcheck](https://cppcheck.sourceforge.io/manual.html),
[GCC analyzer](https://gcc.gnu.org/onlinedocs/gcc/Static-Analyzer-Options.html),
[Clang analyzer](https://clang.llvm.org/docs/ClangStaticAnalyzer.html),
and [Valgrind platforms](https://valgrind.org/info/platforms.html).
