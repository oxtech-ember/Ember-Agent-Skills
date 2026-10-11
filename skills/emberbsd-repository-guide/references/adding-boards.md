# Board workflow

The OS owns the procedure. Set `os` to its checkout; read applicable AGENTS.md,
`ember/boards/adding-a-board.md`, `ember/boards/README.md` and the closest board:

```sh
rg --files "$os/ember/boards" "$os/ember/boot"
rg -n "$board_or_soc" "$os/sys/arch" "$os/sys/dev" "$os/ember"
```

Record model/revision, SoC/architecture, RAM, boot storage, serial settings,
firmware chain and DT/ACPI interface. Compare actual wiring, PHY, storage, power
and radio firmware with vendor documents. A shared SoC proves no peripheral.
Continue source/build work while missing target access blocks hardware checks.

Integrate kernel configuration, DTS/ACPI, drivers, build outputs, boot selection
and regressions in OS. Inspect its builders: a new DTS alone does not add a DTB
to the bundle or loader. Do not reapply fork patches already present. Preserve
bindings, ABIs, firmware licensing and source provenance; route external
libraries to Ports and standalone demonstrations to Examples.

Use the owning architecture's documented builder. Record source/configuration,
compiler, firmware and output hashes; keep kernel/modules/DTBs coherent. Identify
the loader-selected artifact (QEMU `-kernel` can differ from guest `/netbsd`).
Run common-path regressions and useful device scenarios: checked storage/network
transfers, watchdog reset, captured/played audio. Flash/reboot only within task
scope, after identifying the device and recovery path.

Add one board page with a two-column capability table and concise catalog/README
entry. Record date, revisions, workload/duration, measurements, failures and
untested interfaces. Label source/build/VM/hardware evidence separately. Submit
code, boot/build integration, checks and documentation together through
[contributions](contributions.md); use a draft for missing required validation.
Keep board-specific facts in OS, reusable decisions in this skill.
