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
