# Repository ownership

Use this map when task ownership is unclear.
Verify the selected repository's implemented commands and interfaces.

| Repository | Owns |
| --- | --- |
| [EmberBSD](https://github.com/oxtech-ember/EmberBSD) | OS, drivers, boards, firmware integration, system builds |
| [EmberBSD-DevBoards](https://github.com/oxtech-ember/EmberBSD-DevBoards) | Hardware references for boards, carriers, SoCs, interfaces, and bootloaders |
| [EmberBSD-Ports](https://github.com/oxtech-ember/EmberBSD-Ports) | Recipes, source hashes, patches, pkgsrc overlays, dependency profiles |
| [EmberBSD-Examples](https://github.com/oxtech-ember/EmberBSD-Examples) | Public applications and reproducible demonstrations |
| [EmberBSD-Runtime](https://github.com/oxtech-ember/EmberBSD-Runtime) | Planned application execution and lifecycle tools |
| [EmberBSD-SDK](https://github.com/oxtech-ember/EmberBSD-SDK) | Prebuild SDK workspace tools, sysroot orchestration and planned application contracts |
| [Ember-Agent-Skills](https://github.com/oxtech-ember/Ember-Agent-Skills) | Developer AI skills, adapters, packaging |
| [EmberBSD-User-Skills](https://github.com/oxtech-ember/EmberBSD-User-Skills) | Device operations, diagnostics, personal changes, user GitHub work |

DevBoards helps developers adapt reference platforms to their own devices.
Start with its [reader guide](https://github.com/oxtech-ember/EmberBSD-DevBoards/blob/main/docs/reader-guide.md) and [catalog](https://github.com/oxtech-ember/EmberBSD-DevBoards/blob/main/catalog.json).
Check current support in the [OS board catalog](https://github.com/oxtech-ember/EmberBSD/tree/main/ember/boards).
OS and Ports remain the owners of implementation and executable checks.

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
