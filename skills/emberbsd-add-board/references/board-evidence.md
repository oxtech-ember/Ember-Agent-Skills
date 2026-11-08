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
Reuse records of the same board revision and carrier.
For custom devices, read the design transfer notes.
Keep hardware descriptions, boot layouts, and current support limits in DevBoards.
Keep software contracts, builders, and executable checks beside their implementation.
OS image guides describe builder mechanics; DevBoards defines hardware applicability.
Exclude test diaries and duplicate catalogs.

## Driver and subsystem ownership

Assign shared protocols, state machines, cryptography, retries, selection, and rendering policy to common owners.
Assign hardware and vendor interface translation, capabilities, errors, bounds, and security to drivers.
Expose offload through common contracts; retain required device-specific backends and asynchronous transports.
Extend missing common APIs, adapt consumers, and remove duplicate policy as part of the extension.
Add the hardware adapter after the common behavior is ready.
Reuse common regressions and test the hardware boundary.

Record SoC, architecture, RAM, storage, console, firmware chain, and DT/ACPI.
Compare wiring, PHY, storage, power, and radio firmware with vendor documents.
Inspect existing fork patches before applying another copy.
Preserve bindings, ABIs, firmware licenses, and source attribution.
Keep libraries in Ports and demonstrations in Examples.

Use the architecture's documented builder.
Record the [input key](https://github.com/oxtech-ember/EmberBSD-SDK/blob/main/docs/input-keys.md), firmware revision, and artifact hashes.
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

Run [source and memory checks](board-validation.md) for changed drivers and board code.

## Board layer

Update the board to the current package stack first.
Reuse stack evidence when its input key matches; otherwise repeat the affected stack checks.
Test the board's kernel, DTB, display, GPU driver, radio, and firmware integration.
Shared SAE acceptance does not validate another radio chip.
Install no development tools.
Put pins, power, reset, MAC, and region in DT or ACPI.
Use `mmc-pwrseq-simple` for SDIO power.
Pass hardware differences through generic properties and operation tables.
Move logic that two drivers need into a shared helper first.
