# Board evidence

Set `os` to the source checkout.
Inspect the closest implementation.

```sh
rg --files "$os/ember/development" "$os/ember/boot" "$os/ember/image" "$os/ember/tools"
rg -n "$board_or_soc" "$os/sys/arch" "$os/sys/dev" "$os/ember"
```

Start with the [DevBoards reader guide](https://github.com/oxtech-ember/EmberBSD-DevBoards/blob/main/docs/reader-guide.md) and [catalog](https://github.com/oxtech-ember/EmberBSD-DevBoards/blob/main/catalog.json).
Read exact board, carrier, SoC, and bootloader records.
For missing profiles, inspect vendor sources and the closest OS implementation.
Check revisions and applicability before reuse.
For custom devices, read the design transfer notes.
Keep hardware descriptions, boot layouts, and current support limits in DevBoards.
Keep software contracts, builders, and executable checks beside their implementation.
OS image guides describe builder mechanics; DevBoards defines hardware applicability.
Exclude test diaries and duplicate catalogs.

Record SoC, architecture, RAM, storage, console, firmware chain, and DT/ACPI.
Compare wiring, PHY, storage, power, and radio firmware with vendor documents.
Inspect existing fork patches before applying another copy.
Preserve bindings, ABIs, firmware licenses, and source attribution.
Keep libraries in Ports and demonstrations in Examples.

Use the architecture's documented builder.
Record source, configuration, compiler, firmware, and artifact hashes.
Keep kernel, modules, and DTBs coherent.
Identify the loader-selected kernel.
QEMU `-kernel` can differ from guest `/netbsd`.

Run useful storage and network transfers with checked output.
Check watchdog reset and actual audio capture or playback when relevant.
Identify the target device and recovery path before writes.
Record date, revisions, workload duration, measurements, failures, and untested interfaces.

Update the DevBoards profile with supported scenarios, limits, and sources.
Submit implementation and profile changes to their owners when authorized.
Use a draft when required validation remains unavailable and the target permits drafts.

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

## Board layer

Update the board to the current package stack first.
Reuse stack evidence only with matching revisions, ABI, package hashes, and checks.
Repeat affected stack checks after shared changes.
Test the board's kernel, DTB, display, GPU driver, radio, and firmware integration.
Shared SAE acceptance does not validate another radio chip.
Install no development tools.
Put pins, power, reset, MAC, and region in DT or ACPI.
Use `mmc-pwrseq-simple` for SDIO power.
Do not test board or driver names in shared code.
Move logic that two drivers need into a shared helper first.
