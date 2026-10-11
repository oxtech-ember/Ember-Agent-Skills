# Application checks

Set `app`, `examples`, `sdk`, and `runtime` to actual checkouts.
Inspect their tracked files and interface definitions.

```sh
git -C "$app" status --short
rg --files "$app" "$examples" | rg '(^|/)(README[^/]*|Makefile|CMakeLists\.txt|meson\.build|.*test[^/]*)$'
rg -n "$required_interface" "$sdk" "$runtime" "$examples"
```

For `rg`, status 1 means no match.
Status 2 means a failed search.
Check each exit status before the next dependent command.

Read the matching example's README and build definition.
Use its documented commands and dependencies.
An application change usually needs no OS rebuild.
Check the selected target's actual compiler and loaded runtime.
Record expected output and one useful failure case.
State which checks need unavailable hardware.
Store the test receipt beside the application.

Use public fixtures in shared examples.
Make device names and configuration parameters replaceable.
Preserve source attribution.
Route OS defects to [EmberBSD](https://github.com/oxtech-ember/EmberBSD).
Route dependency recipes to [Ports](https://github.com/oxtech-ember/EmberBSD-Ports).
Route public demonstrations to [Examples](https://github.com/oxtech-ember/EmberBSD-Examples).

Verify [SDK](https://github.com/oxtech-ember/EmberBSD-SDK) and [Runtime](https://github.com/oxtech-ember/EmberBSD-Runtime) implementations before use.
Planned Wasm formats and hardware adapters supply no executable interface.
Project names do not establish an `ember` command or MCP server.
The AI plugin catalog and the proposed device application catalog serve different purposes.
