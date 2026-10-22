# Design principles

Apply these principles to every shared OS, Ports, or example change.

## Design first

Design the layers and interfaces before you write code.
Select the simplest and most elegant structure, not the first structure that works.
This is most important for drivers and subsystems.

## Follow the BSD way

- Attach drivers through autoconf(9) and config(5): match, attach, detach, and `files.*` options.
- Describe hardware in FDT bindings or ACPI, not in driver code.
- Use `mmc-pwrseq`, regulators, and GPIO bindings for device power and reset.
- Load firmware through firmload(9).
- Build wireless drivers on net80211 and display drivers on DRM and its helpers.
- Add or update a man page for each new interface.
- Follow style(9) and NetBSD KNF.

## Do not repeat code

If a related driver or script already has the logic, move it to a shared layer first.
Then write the new code on top of that layer.
Do not copy a function and change its prefix.

## Fix the cause

Do not add workarounds.
Fix the base component that causes the fault.
A workaround does not complete a fix.

## Keep code modular and portable

Make each part possible to disable:

- Use a kernel configuration option or an optional attach.
- Do not add hard dependencies between optional parts.
- Make userland features configurable.

Make each part possible to reuse:

- Put common logic in shared subsystem helpers.
- Use clean interfaces and operation tables between layers.
- Do not test for a specific board or driver in shared code.
  For example, do not use `device_is_a("bwfm")` in platform code.
  Set a generic `mac-address` device property instead.

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

- Display: SoC KMS driver, shared DRM helpers for hotplug, EDID, polling, and vblank.
- Graphics: one Mesa package with all GPU drivers; one Qt, KDE Frameworks, and Plasma stack.
- Wi-Fi: one net80211 FullMAC layer, one firmware loader, and one MAC and region path.
  The chip driver contains only its firmware protocol.

## Use one stack and one sysroot

- Build one current package stack in one shared build directory.
- Do not keep separate package sets or accepted snapshots for each device.
- Update a device to the current stack before you test it.
- Keep one clean and current sysroot. Clean and rebuild it when it has stale packages or metadata.
- Accept the stack once. On each device, test only its own layer: kernel, DTB, display, and GPU driver.
- Split packages into runtime and development parts. Install only runtime parts on devices.
