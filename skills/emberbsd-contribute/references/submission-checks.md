# Submission checks

Apply the [SDK tool selection policy](https://github.com/oxtech-ember/EmberBSD-SDK/blob/main/docs/tool-selection.md) to build evidence.
Reject implicit system tools, including native host compilers.
Keep Clang analysis and diagnostic fuzz evidence separate from ordinary GCC16 builds.

Read current upstream instructions before choosing a channel.
A GitHub mirror can accept only mailing-list patches or problem reports.
Use a topic branch and a fork when upstream branch access is absent.
Inspect remotes without exposing embedded credentials.
Preserve unrelated changes, authorship, licenses, and private material.
Keep shared dependency fixes in Ports, separate from private application behavior.
Check existing PRs before preparing a duplicate repair.
Submit through an authorized fork or topic branch after the required checks.
Without publication permission, present the ready patch and evidence before requesting it.
Respect a refusal without claiming the repair is publicly available.

Retain a failing-before and passing-after regression for a code repair.
A port needs build, installed-consumer, and runtime evidence.
A package claim also needs install, remove, and reinstall checks.
Documentation needs command and link checks.
Record unavailable validation separately from failures.
Use drafts only when the target permits them.

Lead the description with the problem and resulting behavior.
Use the repository template.
Include tested revision, platform, tools, commands, results, limits, and provenance.
Address reviews in the same contribution.
Report prepared, submitted, reviewed, merged, or released state accurately.
Verify the normal build from clean source revisions without hidden files or manual patching.
Reuse evidence only when the submitted revision retains the tested inputs.

Keep EmberBSD integration in the project change.
Prepare a minimal upstream patch against upstream's accepted base.
Test that patch separately.
Cross-link authorized submissions.
Use an authorized issue for a reproduced bug without a fix.

Read current [pkgsrc submission rules](https://www.netbsd.org/docs/pkgsrc/submit.html).
Read the [NetBSD AI policy](https://www.netbsd.org/developers/commit-guidelines.html) before submission.
The 2026-10-06 policy required prior written core approval for committing LLM-generated code.
Recheck that rule.
Disclose assistance.
Tests do not replace the accepting project's approval.

## Source and memory analysis

For C/C++ changes, include Cppcheck results for the affected source and tests.
For ports, compare the pinned upstream sources with the patched sources.
Do not require executable checks for documentation-only changes.
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
