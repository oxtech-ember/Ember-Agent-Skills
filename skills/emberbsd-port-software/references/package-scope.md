# Select a package scope

Choose explicit, versionless `PKGPATH` roots for the requested target/ABI. The
existing Ports graph resolves their target dependencies and native host tools.
The full source catalog is not a request to build every package or platform.

Plasma, additional languages, firmware, documentation, and diagnostics are
optional package groups. Keep each group as roots over the common Ports
recipes. Do not add recipe copies, version pins, another resolver, or a private
prefix.

Reuse compatible prefixes, sysroots, packages, and objects by the
[SDK input key](https://github.com/oxtech-ember/EmberBSD-SDK/blob/main/docs/input-keys.md).
Build only missing or incompatible packages in the selected dependency closure.
Package roots do not select a board, ABI, or compiler. Choose those inputs
independently and check compatibility.

Follow the [SDK tool-selection policy](https://github.com/oxtech-ember/EmberBSD-SDK/blob/main/docs/tool-selection.md).
