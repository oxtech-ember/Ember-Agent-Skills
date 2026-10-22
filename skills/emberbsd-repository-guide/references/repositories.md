# Repository ownership

Use this map when task ownership is unclear.
Verify the selected repository's implemented commands and interfaces.

| Repository | Owns |
| --- | --- |
| [EmberBSD](https://github.com/oxtech-ember/EmberBSD) | OS subsystems, drivers, firmware integration, source build rules, software contracts, executable checks |
| [EmberBSD-DevBoards](https://github.com/oxtech-ember/EmberBSD-DevBoards) | Hardware, SoCs, carriers, interfaces, bootloaders, layouts, and current support limits |
| [EmberBSD-Ports](https://github.com/oxtech-ember/EmberBSD-Ports) | Recipes, source hashes, patches, pkgsrc overlays, dependency profiles |
| [EmberBSD-Examples](https://github.com/oxtech-ember/EmberBSD-Examples) | Standalone applications and reproducible demonstrations |
| [EmberBSD-Runtime](https://github.com/oxtech-ember/EmberBSD-Runtime) | Planned application execution and lifecycle tools |
| [EmberBSD-SDK](https://github.com/oxtech-ember/EmberBSD-SDK) | Build orchestration, sysroots, release kits, workspace tools, and planned application contracts |
| [Ember-Agent-Skills](https://github.com/oxtech-ember/Ember-Agent-Skills) | Developer AI skills, adapters, packaging |
| [EmberBSD-User-Skills](https://github.com/oxtech-ember/EmberBSD-User-Skills) | Device operations, diagnostics, personal changes, user GitHub work |

DevBoards helps developers adapt reference platforms to their own devices.
Start with its [reader guide](https://github.com/oxtech-ember/EmberBSD-DevBoards/blob/main/docs/reader-guide.md) and [catalog](https://github.com/oxtech-ember/EmberBSD-DevBoards/blob/main/catalog.json).
Read the exact DevBoards profile for current support and configuration applicability.
Keep hardware descriptions and boot layouts there, including hardware material found in OS image guides.
Keep builder mechanics, API documentation, and executable checks beside the OS or Ports implementation.
Link to the canonical profile instead of creating another support catalog or test diary.
Keep OS documentation with its subsystem, not as an umbrella for other projects.
Keep shared build orchestration, sysroots, and release kits in SDK.
Read its [OS release](https://github.com/oxtech-ember/EmberBSD-SDK/blob/main/docs/os-release.md)
and [AArch64 sysroot release](https://github.com/oxtech-ember/EmberBSD-SDK/blob/main/docs/aarch64-sysroot-release.md) contracts.
Keep dependency recipes and upstream patches in Ports.
Keep standalone UI applications in Examples or their own repository.
Keep skills as concise routes to these owners, without copied implementation contracts.

Find an existing checkout first.
Set `repo` to its path.
Inspect tracked files and relevant definitions.

```sh
git -C "$repo" ls-files
rg -n "$interface_or_command" "$repo"
```

SDK implements workspace tools and sysroot orchestration. Runtime remains in design.
Check sources or releases before calling an API.
Project names do not establish an `ember` CLI or hardware MCP server.
Neither skills package implements an on-device agent.
Use public project sources.
A private wiki is not a prerequisite.
