# Static userland

Use for fixed images/recovery/appliances. Historical Pi 5 acceptance on
2026-10-10/11 used OS revision `383e2a9dc502eeddab2abb6a628580737cbba0b3`:
static rc completion +8s versus dynamic +6s; archive 144MiB versus 36MiB.
Static linking removes loader/library synchronization, not boot time.

## Select and build

Read the owning OS `ember/boot/aarch64-base-update.md`. Extend its reduced profile
with these `build.sh -V` values; retain `INSTALLSETS=base` and normal file checks:

```text
MKPIC=no MKPICINSTALL=no MKPIE=no LDSTATIC=-static MKZFS=no MKDTRACE=no
```

`LDSTATIC` selects the static link; non-PIE avoids unavailable `crt*S.o`.
ZFS/DTrace are excluded for their static-link incompatibilities; leave kernel
`MKCTF` unchanged. Verify the actual [compiler/runtime](ports.md); kernel-only
GCC16 frontends do not supply a complete static base runtime.

Build complete host tools without the reduced `MKGCCCMDS=no` profile: GCC target
libraries need its generated headers, including `insn-constants.h`. Reuse that
TOOLDIR with a separate static obj/dest tree and regenerate `makewrapper`; do
not run reduced `tools`. Inspect generated wrappers for their real TOOLDIR.

Historical clean-build failures to recheck in the owning make rules:

| Component | Missing/generated input |
| --- | --- |
| am-utils/libamu | `config_local.h` |
| GCC libobjc/crtstuff | options/tconfig/runtime/insn/gthr headers |
| GCC libstdc++ | `bits/largefile-config.h` |
| OpenSSL; fetch | `buildinf.h`; `ftperr.h`, `httperr.h` |
| sysinst; boggle; ACPICA | `sysinstmsgs.fmtcnt`; `dictionary`; `dtparser.y.h` |
| libpam; rescue | `openpam_static.o`; `liboverride.o` |
| DTBs; efiboot | kernel-produced DTBs; global static link rejects EFI PHDR layout |

Fix missing generation dependencies in OS. For bounded recovery, invoke the
actual generation target with its make wrapper; reuse outputs only with matching
source/configuration provenance. Diagnose host compiler crashes and its Ports
math dependencies; a retry is not a compatibility fix. Keep recovery in owning
tools, not a copied shell sequence in the skill.

## Inspect and deploy

Check candidate archive/binaries before any installation:

```sh
tar -tf "$base_set" > "$listing"
rg '(\.so([./]|$)|ld\.elf_so)' "$listing"
file "$candidate/bin/sh"
```

Require successful archive listing, `rg` status 1 (no shared libraries/loader),
and a statically linked shell; status 2 is a failed search. For authorized
deployment follow the OS recovery/install procedure: coherent artifacts, chroot
checks with the target MAKEDEV definition, rollback archive, hashed board-radio
firmware overlay, and a new SSH login after restarting critical services before
reboot. Archive extraction does not remove obsolete `.so` files. Check loaded
kernel revision, memfd/FP contracts and network afterward. Historical static
sshd/public-key, dhcpcd and WPA3/SAE results qualify that Pi 5 only; record actual
revision, sets/hashes, commands, results and limits for each new deployment.
