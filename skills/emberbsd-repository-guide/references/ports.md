# Ports and current development tools

Read this for third-party software, dependency upgrades, or build failures.
The owning source of recipes and validation is
[EmberBSD-Ports](https://github.com/oxtech-ember/EmberBSD-Ports), not this skill.

## Choose and pin the source

- Verify the current stable upstream release from an original release page.
  Distinguish a supported LTS choice with a concrete reason from an obsolete
  package retained merely because it builds. Record the verification date.
- Check the pinned pkgsrc base and current pkgsrc/pkgsrc-wip before writing a
  new recipe. Reuse their relevant work and preserve authorship and licenses.
  Pin the exact revision; do not build an unrecorded moving HEAD.
- Keep original download URLs, versions, SHA256, recipe parameters, and patch
  provenance in Ports. Verify archives before extraction. A mismatch is an
  error to investigate, not a reason to replace the expected hash.
- Keep the small delta over pkgsrc. Use ordinary package recipes, dependency
  declarations, staging and package tools; do not invent another package manager.
  Upstream trees, archives, caches and binaries stay outside Git history.
- Fix source, recipe and ABI incompatibilities in versioned Ports sources.
  A repair left only inside a build VM is incomplete.

## Keep the development profile coherent

Current EmberBSD development profiles include current stable compilers and build
tools, plus Ruby, Go and TinyGo. Recheck versions for each upgrade; a version
listed in an old conversation is not a permanent pin.

Build the new compiler with a recorded bootstrap compiler, then rebuild its
affected dependency closure. A temporary bootstrap or recovery compiler is not
the final image's default development environment. Changes to the system image
and base toolchain belong to the OS repository and need their own checks.

For C++ libraries, inspect both DT_NEEDED and the runtime actually loaded.
Do not disguise one libstdc++ SONAME as another. Do not accept two C++ runtimes
in one process. Test object exchange, exception unwinding and representative
consumers such as Qt or LLVM after a compiler/runtime change.

Choose current common dependencies and adapt their consumers. If an upstream
requires a private fork, inspect its patches and supported targets before
replacing it with a shared library. Preserve functionality rather than silently
dropping a backend to make the build green. Document any temporary restriction
and its removal condition; do not label the restricted result fully supported.

## Select host and target compilers

Record the resolved executable, version and target triplet for each compiler
before building. Inspect CMake/Meson caches as well as `CC`, `CXX`, `HOST_CC`
and the cross prefix. A preinstalled Linux compiler is an environment input;
it does not define EmberBSD's development profile. Select the current Ports
GCC16 explicitly for the requested development workflow. Keep a recorded older
bootstrap compiler confined to the stage that requires it.

At OS revision `ea4addbc8543cad1f3d0abe2cec1dd4b47ef9cbb`, `build.sh` still
bootstraps GCC 12.5. The kernel wrapper's cross mode alone therefore does not
select GCC16. Its `EMBER_EXTERNAL_TOOLCHAIN` selects the GNU cross prefix;
changing the host's `PATH` or `CC` alone is insufficient. Recheck the
[OS cross-build guide](https://github.com/oxtech-ember/EmberBSD/blob/main/ember/boot/cross-build.md)
and the actual wrapper when this source revision changes.

Choose prerequisites by artifact:

| Artifact | Required target inputs |
| --- | --- |
| Kernel and modules | The fork's sources, generated kernel headers and matching cross compiler/binutils; no inherent dependency on an installed userland or C++ runtime |
| Linked C/C++ applications | A provenance-checked EmberBSD sysroot with target libc, startup objects and the selected GCC16 headers/runtime |
| Host contracts and build generators | Host executables and host libraries; target binaries cannot run merely because their CPU architecture matches |

The [Ports GCC16 cross recipe](https://github.com/oxtech-ember/EmberBSD-Ports/tree/main/profiles/development-toolchain/cross)
offers a `--kernel` mode without a userland sysroot; its application mode still
requires provenanced target libc, startup objects and headers/runtime. Use the
owning recipe instead of creating a private compiler helper or a dummy/mixed
sysroot. Its host-math helper selects the language mode needed by GMP6.3.0
and runs the upstream dependency tests while retaining the selected compiler.
Keep compiler/runtime compatibility repairs in Ports and source-contract fixes
in the OS, then recheck their callers. Skills select these implementations;
they do not duplicate temporary setup workarounds.

## Test what a developer will use

| Change | Useful acceptance evidence |
| --- | --- |
| C/C++ compiler | Compile, link and run code with atomics, threads, TLS, and shared-library exception boundaries; inspect actual runtime resolution |
| Ruby | Run Ruby and package tests; build and load a native extension using the selected compiler |
| Go | Build and test a module, including cgo where supported; record bootstrap and actual compiler paths |
| TinyGo | Build a Wasm/WASI program and run it with a compatible runtime; separately compile selected MCU targets and distinguish compilation from flashing or a board test |
| Ordinary port | Upstream tests, regression for each local fix, staged package/install checks and a meaningful user workflow |
| Shared library | Affected direct and transitive consumers, loader identity, clean shutdown and repeated use where lifetime changed |
| Model engine | Installed C/C++ consumer, selected execution provider, known numerical output, invalid model/input rejection and bounded execution |
| Streaming audio/video | Explicit backend, actual samples/frames and timestamps, state across input chunks, end-of-stream and damaged-input handling |

Keep real exit statuses. Do not accept stale output from a failed build, suppress
unexplained warnings, replace unavailable behavior with success stubs, or report
a skipped device test as a pass. Record the revision, configuration, commands,
results and artifact hashes. Full logs may stay in a private artifact store;
include enough non-sensitive evidence to reproduce the result publicly.

Coordinate shared build machines before changing compilers, libraries or VM
configuration. Measure free disk and RAM, limit workers, and retain a recovery
path. Reboots and device writes must be within the task's authorized scope.

## Verified lessons to recheck when they apply

- **TinyGo from pkgsrc-wip:** revision
  [30b5c392](https://github.com/NetBSD/pkgsrc-wip/tree/30b5c39233c7affa55f3db0a692457e16c127181/tinygo)
  packages 0.42.0 with NetBSD adaptations and a bundled LLVM fork.
  The [0.42.0 release](https://github.com/tinygo-org/tinygo/releases/tag/v0.42.0)
  supports Go 1.27 and LLVM 22. Checked 2026-10-06. LLVM 23 compatibility and
  native EmberBSD execution require testing; recipe presence proves neither.
- **Graphics evidence:** software EGL readback, KMS scanout, native Wayland
  input, and host GPU rendering are separate claims. See the current
  [Wayland probe](https://github.com/oxtech-ember/EmberBSD-Ports/tree/main/probes/wayland-utm)
  for its exact tested limits. A nested desktop or software renderer cannot
  establish hardware acceleration.
- **OpenCV 5.0.0 on NetBSD AArch64 with GCC:** a completed build aborted before
  `main` because runtime detection missed the required NEON/FP16 conversion
  baseline. The [tested patch and regression](https://github.com/neonix20b/EmberBSD-Ports/blob/23975050ad678e85e56d1379107f7bbc10c0a2b7/probes/robotics-foundations/PROVENANCE.md)
  restore baseline detection without disabling its guard. Optional FP16
  arithmetic, DotProd, BF16 and SVE remain unadvertised. Checked 2026-10-06 in
  an EmberBSD AArch64 VM; the patch has not been submitted upstream. Recheck
  detection in a newer release and drop the patch when the regression passes
  without it. Do not generalize this into disabling CPU optimizations.
- **gpsd 3.27.5 PTY tests in a single-user VM:** missing ptyfs caused PTY
  allocation to fail. Ordinary test-environment preparation fixed it without
  a gpsd source patch. Check the environment before changing library code.
  The [installed probe](https://github.com/neonix20b/EmberBSD-Ports/blob/23975050ad678e85e56d1379107f7bbc10c0a2b7/probes/robotics-foundations/README.md)
  documents prerequisites and synthetic NMEA tests. OpenCV 5.0.0, Eigen 5.0.1
  and gpsd 3.27.5 passed six installed-consumer checks there on 2026-10-06.
  This is source-probe evidence, not pkgsrc packaging, camera/GNSS hardware
  support or a full upstream OpenCV/Eigen test run. Recheck prerequisites for
  the actual boot mode; do not prescribe remounting on every gpsd failure.

- **Current media on NetBSD AArch64:** FFmpeg 9.0.2 needs explicit PIC for
  shared libraries. OpenCV 5.0.0 needs the accepted FFmpeg 9 API backport and
  a local guard fix enabling its existing POSIX filesystem path on NetBSD;
  otherwise GStreamer capture can fail at `exists()` after a successful build.
  The [media provenance and regressions](https://github.com/neonix20b/EmberBSD-Ports/blob/aed5293/probes/media/PROVENANCE.md)
  record each change. Both installed videoio backends passed file workflows
  on 2026-10-07. Recheck newer upstream releases before carrying these changes
  forward. The profile excludes V4L because of separate header incompatibility;
  it does not establish camera capture or justify silently dropping a camera
  backend from a task that requires it.
- **GLib metadata and runtime ABI:** tested GLib 2.88.1 used base libintl,
  while bare `-lintl` in pkg-config selected an additional pkgsrc ABI. The
  [media recipe](https://github.com/neonix20b/EmberBSD-Ports/blob/aed5293/probes/media/build.sh)
  checks ELF dependencies before correcting a private metadata copy. Verify
  the actual package and loaded libraries; do not apply this correction to
  every GLib installation or disguise ABIs with symlinks. Remove it when
  the selected package metadata agrees with its real dependency.
- **Complete frames do not prove a complete container:** the media regression
  originally accepted Matroska with a truncated trailer because all frames
  decoded. For a trusted fixture, compare its known length and diagnostics as
  well as pixels, timestamps and EOF. Do not claim a general container validator
  from this bounded fixture check.
- **RNNoise 0.2 ARM build:** the release references an absent Opus header.
  The accepted upstream fix
  [372f7b4b](https://github.com/xiph/rnnoise/commit/372f7b4b76cde4ca1ec4605353dd17898a99de38)
  restores the ARM build using RNNoise's own equivalents. Preserve its author
  and unchanged patch rather than disabling NEON or supplying success stubs.
  Recheck whether the selected release already contains it. A deterministic
  sample/state contract establishes execution, not noise-reduction quality;
  the latter needs a suitable speech/noise corpus and explicit metrics.
- **Cross-built network diagnostics kit:** libpcap, tcpdump, iperf3, the
  Wireshark 4.6.8 CLI set and the native `hcisnoop` BTSnoop recorder are
  [packaged and board-verified](https://github.com/oxtech-ember/EmberBSD-Ports/tree/main/profiles/network-diagnostics)
  on Raspberry Pi 5: live BPF capture without kernel drops, a three-file
  dumpcap ring buffer under load with drop accounting, TCP/UDP iperf3
  against a LAN peer, and a real Bluetooth controller inquiry with correct
  host/controller directions (checked 2026-10-10). The cross build needed
  lessons that recur in other ports: pkgsrc `PKG_OPTIONS` only add to the
  suggested set, so disable each unwanted option explicitly; recipes that
  set `CC_FOR_BUILD=${NATIVE_CC}` need that variable pinned or their
  build-time generators become unrunnable target binaries; `REPLACE_SH` and
  awk substitutions bake build-host paths into target scripts unless the
  platform tools resolve to paths valid on both sides; CMake consumers need
  explicit target system, sysroot and find-root arguments; parser generators
  such as lemon must be built for and run on the build host. Recheck each
  against the current profile instead of copying the workarounds blindly.

When those sources advance, recheck the affected case and update this reference.
Keep detailed recipes and executable regressions with their owning port.
