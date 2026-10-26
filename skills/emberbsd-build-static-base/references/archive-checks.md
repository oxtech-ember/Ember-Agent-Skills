# Archive and deployment checks

Set `base_set`, `listing`, and `candidate` to the actual outputs.

```sh
tar -tf "$base_set" > "$listing"
rg '(\.so([./]|$)|ld\.elf_so)' "$listing"
file "$candidate/bin/sh"
```

Require a successful archive listing and a statically linked shell.
For the search, status 1 means no shared libraries or loader were found.
Status 2 means the search failed.
Archive extraction does not remove obsolete `.so` files.

For authorized deployment, follow the OS recovery and installation procedure.
Keep coherent artifacts, chroot checks, target MAKEDEV definitions, and a rollback archive.
Record hashes for the board radio firmware overlay.
After restarting critical services, verify a new SSH login before reboot.
Then check the running kernel revision, memfd, floating-point contracts, and network.
Record set hashes, commands, results, and gaps.

Historical Pi5 acceptance on 2026-10-10/11 used OS revision `383e2a9dc502eeddab2abb6a628580737cbba0b3`.
Static rc completion took about eight seconds; dynamic rc completion took about six seconds.
The archives measured 144MiB and 36MiB respectively.
Static linking removes loader and library synchronization requirements.
Those measurements do not establish faster boot.
Recorded static sshd, public-key login, dhcpcd, and WPA3/SAE results qualify only that tested Pi5 configuration.

## Source and memory analysis

For changed C/C++ base components, run Cppcheck on the selected sources.
Compare imported source findings before and after portability patches.
Static linkage alone does not prove memory safety.
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
