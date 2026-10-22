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

## Do not repeat code

Use existing subsystem helpers first.
Extract missing shared behavior before adding consumers.
Matching function names do not justify a shared FullMAC firmware abstraction.

## Fix the cause

Fix the component that causes the fault.
Do not add workarounds.

## Keep code modular and portable

Allow each part to be disabled:

- Use a kernel configuration option or an optional attach.
- Do not add hard dependencies between optional parts.
- Make userland features configurable.

Allow each part to be reused:

- Put common logic in shared subsystem helpers.
- Use clean interfaces and operation tables between layers.
- Do not test for a specific board or driver in shared code.
  Use generic device properties such as `mac-address`.

## Separate layers and responsibilities

| Layer | Contains | Does not contain |
| --- | --- | --- |
| Chip driver | Chip and bus protocol, registers, firmware format | Subsystem logic, board facts |
| Shared subsystem helper | Logic common to one device class | Chip or board names |
| Board DT | Pins, power, reset, interrupts, MAC, region | Code |
| Userland | One shared service or script with parameters | Copies for each board |
| Build host and sysroot | Compilers, SDK files, headers, analyzers | Device runtime state |
| Device | Runtime packages and its own hardware layer | Development tools |

Examples:

- Display: reuse existing DRM helpers for hotplug, EDID, polling, and vblank.
  Keep hardware IRQ and PHY operations in chip callbacks.
- Graphics: one Mesa package with supported GPU drivers per ABI; one Qt, KDE Frameworks, and Plasma stack.
- Wi-Fi: share net80211 behavior, firmware loading, MAC properties, and region handling.
  Keep chip firmware protocols separate.

## Use one stack and one sysroot

- Build one current package stack with shared objects and packages for each target ABI.
- Keep incompatible ABIs in separate build roots.
- Do not keep separate package sets or accepted snapshots for each device.
- Update a device to the current stack before you test it.
- Each developer maintains one current sysroot per target ABI.
  Build its replacement alongside it when packages or metadata become stale.
  Replace the old sysroot only after the new one passes acceptance.
- Reuse stack acceptance only when its revisions, ABI, package hashes, and checks match.
- On each device, check its kernel, DTB, display, GPU driver, radio, and firmware integration.
  Shared SAE acceptance does not validate another radio chip.
- Repeat affected stack checks after shared changes.
- Split packages into runtime and development parts. Install only runtime parts on devices.
