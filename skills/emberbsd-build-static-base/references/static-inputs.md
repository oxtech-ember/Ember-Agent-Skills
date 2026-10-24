# Static build inputs

Extend the owning reduced base profile with these `build.sh -V` values.

```text
MKPIC=no MKPICINSTALL=no MKPIE=no LDSTATIC=-static MKZFS=no MKDTRACE=no
```

`LDSTATIC` selects static linking.
Non-PIE avoids unavailable `crt*S.o` inputs.
ZFS and DTrace have static-link incompatibilities in this profile.
Leave kernel `MKCTF` unchanged.

Build complete host tools without the reduced `MKGCCCMDS=no` setting.
Target GCC libraries require generated headers, including `insn-constants.h`.
Reuse the complete TOOLDIR with separate static object and destination trees.
Regenerate `makewrapper` for that configuration.
Inspect its actual TOOLDIR.
Do not replace complete tools with a reduced tools build.

Check these historical generation failures in current OS make rules.

| Component | Input |
| --- | --- |
| am-utils/libamu | `config_local.h` |
| GCC libobjc/crtstuff | options, tconfig, runtime, insn, gthr headers |
| GCC libstdc++ | `bits/largefile-config.h` |
| OpenSSL | `buildinf.h` |
| fetch | `ftperr.h`, `httperr.h` |
| sysinst | `sysinstmsgs.fmtcnt` |
| boggle | `dictionary` |
| ACPICA | `dtparser.y.h` |
| libpam | `openpam_static.o` |
| rescue | `liboverride.o` |
| DTBs | Kernel-produced device trees |
| efiboot | EFI PHDR layout rejects global static linking |

Fix generation dependencies at their source.
For bounded recovery, invoke the real generation target through its make wrapper.
Reuse generated outputs only with matching source and configuration records.
Inspect Ports host math dependencies when the host compiler crashes.
Keep recovery commands in owning tools.

Use current Ports recipes for direct, transitive, build, and test dependencies, including host tools.
Follow the [shared dependency contract](https://github.com/oxtech-ember/EmberBSD-Ports/blob/main/docs/update-ports.md) while preserving native OS integration.
Keep base build repairs in OS and shared third-party repairs in Ports.
Prepare regressions and submit an authorized PR through the [contribution procedure](https://github.com/oxtech-ember/EmberBSD/blob/main/CONTRIBUTING.md).
Without publication permission, present the tested patch before asking.
Respect a refusal and report the repair as unsubmitted.
