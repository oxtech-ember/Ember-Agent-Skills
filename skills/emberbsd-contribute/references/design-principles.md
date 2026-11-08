# Design principles

## Design first

Design the layers and interfaces before you write code.
Select the simplest structure.

## Follow the BSD way

- Attach drivers through autoconf(9) and config(5): match, attach, detach, and `files.*` options.
- Describe hardware in FDT bindings or ACPI, not in driver code.
- Use `mmc-pwrseq`, regulators, and GPIO bindings for device power and reset.
- Load firmware through firmload(9).
- Build wireless drivers on net80211 and display drivers on DRM and its helpers.
- Add or update a man page for each new interface.
- Follow style(9) and NetBSD KNF.

## Reuse shared code

Use existing subsystem helpers first.
Extract missing shared behavior before adding consumers.
Reuse [Ports dependencies](https://github.com/oxtech-ember/EmberBSD-Ports/blob/main/docs/update-ports.md).
Matching function names do not justify a shared FullMAC firmware abstraction.

## Keep hardware adapters thin

Assign shared protocols, state machines, cryptography, retries, selection, and rendering policy to their existing subsystem or userland owner.
Assign bus, register, DMA, interrupt, and vendor ABI translation to hardware drivers.
Report hardware capabilities and errors through the subsystem contract.
Enforce bounds and security at the hardware boundary.
Expose hardware offload through the existing common contract and keep one owner for its policy and protocol.
Keep device-specific GPU backends and asynchronous transports where hardware requires them.
Keep their policy contract in the existing subsystem.
When the common API is missing, extend its owner and adapt affected consumers.
Remove duplicated policy as part of that API extension.
Define adapter scope by hardware responsibilities and contract.
Review shared-logic ownership alongside board behavior.
Reuse common regressions and test the hardware boundary.

## Fix the cause

Fix the component that causes the fault.
Repair the owning implementation and verify the affected contract.

## Keep code modular and portable

Keep optional parts disableable and userland features configurable.
Put common logic in shared helpers with clean interfaces and operation tables.
Represent platform configuration through generic device properties such as `mac-address`.

## Separate layers and responsibilities

| Layer | Responsibility | Interface to other owners |
| --- | --- | --- |
| Chip driver | Chip and bus protocol, registers, firmware format | Use subsystem APIs and board properties |
| Shared subsystem helper | Logic common to one device class | Receive capabilities and generic properties |
| Board DT | Pins, power, reset, interrupts, MAC, region | Supply declarative properties to drivers |
| Userland | One shared service or script with parameters | Receive board differences as parameters |
| Build host and sysroot | Compilers, SDK files, headers, analyzers | Produce target artifacts; keep runtime state on devices |
| Device | Runtime packages and its own hardware layer | Keep development tools on the build host |

Examples:

- Display: reuse existing DRM helpers for hotplug, EDID, polling, and vblank.
  Keep hardware IRQ and PHY operations in chip callbacks.
- Graphics: one Mesa package with supported GPU drivers per ABI; one Qt, KDE Frameworks, and Plasma stack.
- Wi-Fi: share net80211 behavior, firmware loading, MAC properties, and region handling.
  Keep chip firmware protocols separate.

For build and package scope, also read [stack and sysroot rules](stack-and-sysroot.md).
