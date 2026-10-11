# Recipe checks

Set `ports` to the owning checkout.
Inspect its pinned package sources before writing another recipe.

```sh
git -C "$ports" submodule status
rg --files "$ports/profiles" "$ports/probes" | rg '(README\.md|sources\.tsv|build\.sh|test.*\.sh)$'
rg -n "$dependency" "$ports/profiles" "$ports/probes"
```

Select current stable upstream or a justified supported LTS release.
Record release date, source revision, original URL, SHA256, and patch authorship.
Verify archives before extraction.
Investigate changed hashes instead of replacing expected values without evidence.
Preserve licenses and required private-fork backends.
Use ordinary pkgsrc recipes, staging, and package tools.

Check CPU, RAM, and disk capacity before setting job limits.
Coordinate access to a shared build host.
Use new outputs after compiler or configuration changes.
Keep actual exit statuses.
A failed build, skipped test, or success stub establishes no pass.

| Change | Required evidence |
| --- | --- |
| Compiler | Atomics, threads, TLS, DSO exceptions, loaded runtime |
| Ruby | Package tests and a loaded native extension |
| Go | Module tests and required cgo paths |
| TinyGo | Actual Wasm/WASI execution or MCU compilation |
| Package | Build, tests, staged install, remove, reinstall |
| Library | Installed consumers, expected result, invalid input, lifecycle |
| Media | Selected backend, frames, timestamps, state, EOF, damaged input |

MCU compilation does not prove flashing or device execution.
Keep device writes within the requested scope.
