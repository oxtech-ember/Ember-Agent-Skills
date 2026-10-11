# Board evidence

Set `os` to the source checkout.
Read the board catalog and closest board page.

```sh
rg --files "$os/ember/boards" "$os/ember/boot"
rg -n "$board_or_soc" "$os/sys/arch" "$os/sys/dev" "$os/ember"
```

Record SoC, architecture, RAM, storage, serial settings, firmware chain, and DT/ACPI interface.
Compare wiring, PHY, storage, power, and radio firmware with vendor documents.
Inspect existing fork patches before applying another copy.
Preserve bindings, ABIs, firmware licenses, and source attribution.
Keep external libraries in Ports.
Keep standalone demonstrations in Examples.

Use the architecture's documented builder.
Record source, configuration, compiler, firmware, and artifact hashes.
Keep kernel, modules, and DTBs coherent.
Identify the loader-selected kernel.
QEMU `-kernel` can differ from guest `/netbsd`.

Run useful storage and network transfers with checked output.
Check watchdog reset and actual audio capture or playback when relevant.
Identify the target device and recovery path before writes.
Record date, revisions, workload duration, measurements, failures, and untested interfaces.

Add one board page with a two-column capability table.
Add a concise catalog or README row.
Submit code, boot integration, checks, and documentation together when authorized.
Use a draft when required validation remains unavailable and the target permits drafts.
Keep board-specific facts in OS documentation.

## Source and memory analysis

Run Cppcheck on changed C/C++ drivers, board code, and executable contract tests.
Valgrind cannot check kernel code or device DMA directly.
Use suitable user-space contracts and target kernel diagnostics.
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
