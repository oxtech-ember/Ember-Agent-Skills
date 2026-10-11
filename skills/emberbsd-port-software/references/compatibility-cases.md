# Conditional compatibility cases

Read only the case that matches the task.
Recheck the selected source before using a historical remedy.
Remove obsolete patches when their regression passes without them.

## TinyGo

Inspect the [pinned pkgsrc-wip recipe](https://github.com/NetBSD/pkgsrc-wip/tree/30b5c39233c7affa55f3db0a692457e16c127181/tinygo).
The 2026-10-06 check recorded TinyGo0.42.0, Go1.27, and LLVM22.
LLVM23 and native EmberBSD acceptance remained open.
Inspect required fork patches before changing LLVM sources.

## Graphics

Use the [Wayland probe](https://github.com/oxtech-ember/EmberBSD-Ports/tree/main/probes/wayland-utm).
Record EGL readback, KMS scanout, input, and host rendering separately.
One path does not establish the other paths.

## OpenCV CPU detection

Read the [robotics provenance](https://github.com/neonix20b/EmberBSD-Ports/blob/23975050ad678e85e56d1379107f7bbc10c0a2b7/probes/robotics-foundations/PROVENANCE.md).
The recorded GCC/NetBSD AArch64 case concerns NEON-FP16 baseline detection.
Preserve the CPU guard.
Do not advertise optional FP16 arithmetic, DotProd, BF16, or SVE from that result.
The patch had no upstream submission at the recorded revision.

## gpsd PTY failure

Check ptyfs and the VM environment before source changes.
Read the [robotics probe](https://github.com/neonix20b/EmberBSD-Ports/blob/23975050ad678e85e56d1379107f7bbc10c0a2b7/probes/robotics-foundations/README.md).
Its six installed-consumer checks on 2026-10-06 establish no physical GNSS or camera support.
They do not establish package lifecycle acceptance.

## Cross-built diagnostics

Read the [network profile](https://github.com/oxtech-ember/EmberBSD-Ports/tree/main/profiles/network-diagnostics).
Its Pi5 capture, drops, ring, TCP/UDP, and Bluetooth evidence dates from 2026-10-10.
Check negative `PKG_OPTIONS` syntax and target script paths.
Pin `NATIVE_CC` or `CC_FOR_BUILD` for host generators.
Check CMake roots and host parser generators separately from target compilers.
