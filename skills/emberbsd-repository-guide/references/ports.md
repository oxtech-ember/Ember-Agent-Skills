# Ports and compiler selection

Use the owning [Ports recipes](https://github.com/oxtech-ember/EmberBSD-Ports).
Keep fixes, dependency declarations, source hashes and executable checks there.

## Inspect and pin

```sh
git -C "$ports" submodule status
rg --files "$ports/profiles" "$ports/probes" | rg '(README\.md|sources\.tsv|build\.sh|test.*\.sh)$'
rg -n "$dependency" "$ports/profiles" "$ports/probes"
```

Verify current stable upstream or a justified supported LTS; inspect pinned
pkgsrc/pkgsrc-wip before writing a recipe. Record release/date/revision, original
URL/SHA256 and patch authorship/license. Verify archives before extraction;
a mismatch needs investigation, not a new expected hash. Use ordinary pkgsrc
recipes/staging/package tools; keep caches, upstream trees and binaries out of Git.

Rebuild the affected dependency closure after compiler/library changes. Inspect
DT_NEEDED and loaded runtimes with target `readelf`/`ldd`; test representative
consumers and exception/object exchange. One process must use a coherent C++
runtime, without fake SONAME symlinks. Inspect private-fork requirements before
replacing them with common libraries; preserve required backends.

## Select host and target compilers

Read `profiles/development-toolchain/cross/README.md` and its scripts. Bind `ports`,
`os`, new pkgsrc export directory `pkgsrc`, original `gcc_archive`, fork-built host `tools`, new
compiler `work` and kernel `output` to absolute paths allowed by those recipes.
Inspect `CC/CXX/HOST_CC/HOST_CXX`, cached build compilers and loaded runtimes.
The preparation command requires a nonexistent export; omit it only when reusing
a verified export from the selected Ports/pkgsrc revision:

```sh
command -v gcc g++
gcc -dumpfullversion
gcc -dumpmachine
g++ -dumpfullversion
g++ -dumpmachine
git -C "$ports" submodule update --init --depth 1 upstream/pkgsrc
sh "$ports/scripts/prepare-pkgsrc.sh" "$pkgsrc" development-toolchain
HOST_CC=gcc HOST_CXX=g++ CROSS_JOBS="$jobs" \
    sh "$ports/profiles/development-toolchain/cross/build.sh" --kernel \
    "$pkgsrc" "$gcc_archive" "$tools" "$work"
"$work/toolchain/bin/aarch64--netbsd-gcc" -dumpfullversion
"$work/toolchain/bin/aarch64--netbsd-gcc" -dumpmachine
HOST_CC=gcc HOST_CXX=g++ CC=gcc NETBSD2_JOBS="$jobs" \
    EMBER_EXTERNAL_TOOLCHAIN="$work/toolchain" \
    sh "$os/ember/build-kernel.sh" "$output" EMBER64
```

Require GCC16 on host and target for this workflow. `jobs` must match available
resources. Kernel mode needs no application sysroot; it builds isolated host
math when no optional prefix is supplied. The recipe documents reusing host math
and the verified GCC archive. The OS bootstrap defaults to GCC12.5; verify the
actual external prefix. Do not silently use GCC12/14 or fabricate/mix sysroots.

Linked applications use the recipe's sysroot mode, `compile-tests.sh` and target
runner, with provenanced libc/startup objects and matching GCC16 headers/runtime.
A kernel-only compiler provides no target application runtime.

## Validate the requested behavior

| Change | Check |
| --- | --- |
| C/C++ compiler | Compile/link/run atomics, threads, TLS and shared-library exceptions; actual loaded runtime |
| Ruby | Package tests plus build/load a native extension |
| Go/TinyGo | Module tests including cgo; Wasm/WASI runtime; MCU compilation distinct from flashing |
| Port/package | Upstream tests, local regressions, staged install/remove/reinstall and useful workflow |
| Library/model engine | Direct/transitive installed consumers, expected numerical/API result, invalid input, lifecycle |
| Streaming media | Selected backend, samples/frames/timestamps, chunk state, EOF and damaged input |

Keep real exit statuses, revision/configuration and artifact hashes. Failed builds,
stale artifacts, success stubs and skipped device tests establish no pass. Bound
jobs using disk/RAM/CPU checks; coordinate shared hosts and keep device writes
within task scope. Submit authorized shared changes via [contributions](contributions.md).

## Conditional pointers to owning regressions

Historical facts below are entry points, not permanent version pins. Recheck the
selected source; retire local patches when their regression passes unpatched.

| Symptom/task | Source and constraint |
| --- | --- |
| TinyGo upgrade | [pkgsrc-wip recipe](https://github.com/NetBSD/pkgsrc-wip/tree/30b5c39233c7affa55f3db0a692457e16c127181/tinygo): 0.42.0/Go1.27/LLVM22 checked 2026-10-06; LLVM23/native EmberBSD needs acceptance |
| Graphics claim | [Wayland probe](https://github.com/oxtech-ember/EmberBSD-Ports/tree/main/probes/wayland-utm): EGL readback, KMS scanout, input and host rendering are separate evidence |
| OpenCV aborts before main | [Robotics provenance](https://github.com/neonix20b/EmberBSD-Ports/blob/23975050ad678e85e56d1379107f7bbc10c0a2b7/probes/robotics-foundations/PROVENANCE.md): GCC/NetBSD AArch64 NEON-FP16 baseline detection, not optional FP16 arithmetic/DotProd/BF16/SVE; guard retained, patch not submitted upstream |
| gpsd PTY failure | [Robotics probe](https://github.com/neonix20b/EmberBSD-Ports/blob/23975050ad678e85e56d1379107f7bbc10c0a2b7/probes/robotics-foundations/README.md): check ptyfs/environment before source edits; six installed-consumer checks on 2026-10-06 prove no camera/GNSS/package support |
| Media builds but fails at runtime | [Media provenance](https://github.com/neonix20b/EmberBSD-Ports/blob/aed5293/probes/media/PROVENANCE.md): FFmpeg9.0.2 PIC; OpenCV5 FFmpeg9 API/POSIX filesystem repairs; file backends tested 2026-10-07, V4L excluded, camera untested |
| GLib libintl mismatch | [Media recipe](https://github.com/neonix20b/EmberBSD-Ports/blob/aed5293/probes/media/build.sh): inspect ELF before metadata correction; base and pkgsrc ABI differ, no blanket correction/symlink |
| Complete frames, truncated container | Media regression: compare trusted length/decoder diagnostics plus pixels/timestamps/EOF; bounded fixture is no general validator |
| RNNoise0.2 ARM missing header | [Accepted upstream fix](https://github.com/xiph/rnnoise/commit/372f7b4b76cde4ca1ec4605353dd17898a99de38): retain attribution/NEON; deterministic state/sample test is no quality metric |
| Cross-built diagnostics | [Network profile](https://github.com/oxtech-ember/EmberBSD-Ports/tree/main/profiles/network-diagnostics): Pi5 capture/drop/ring/TCP/UDP/Bluetooth evidence checked 2026-10-10; inspect negative PKG_OPTIONS, pinned NATIVE_CC/CC_FOR_BUILD, target script paths, CMake roots and host parser generators |
