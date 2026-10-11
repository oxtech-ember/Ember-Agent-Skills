# Application workflow

Work in the user's application repository under its conventions and publication
scope. Identify target board/VM, image/revision, architecture, dependencies and
available test access; request only missing facts that block implementation.

Set `app`, `examples`, `sdk`, `runtime` to actual checkouts. Discover entry points:

```sh
git -C "$app" status --short
rg --files "$app" "$examples" | rg '(^|/)(README[^/]*|Makefile|CMakeLists\.txt|meson\.build|.*test[^/]*)$'
rg -n "$required_interface" "$sdk" "$runtime" "$examples"
```

Read the matching example README and build definition. Use its verified
commands/dependencies rather than rebuilding the OS for an application change.
Inspect SDK/Runtime definitions before calling APIs; design-only contracts and
planned Wasm formats, marketplaces or hardware adapters are unavailable tools.
Use an existing supported path if it satisfies the task; otherwise state the gap.

Run the application's real build, tests and smallest demonstration. Record host
versus target commands, actual tool/runtime identity, expected output, one useful
failure case, and untested hardware. Keep this receipt beside the application.
Examples need public fixtures and replaceable device/configuration parameters;
preserve attribution when adapting code.

Route third-party compatibility to [Ports](ports.md), OS defects to the OS,
and standalone demonstrations to Examples. Publish a minimal reusable fix via
[contributions](contributions.md) when authorized; private application material
stays private. Ordinary application work does not require a PR or authorize
flashing. Update affected [guidance](maintenance.md) after verified changes.
