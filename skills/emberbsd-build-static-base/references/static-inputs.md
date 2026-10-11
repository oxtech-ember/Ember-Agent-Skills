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
