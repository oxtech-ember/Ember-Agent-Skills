# Repository ownership

Use this map to route changes; verify implementations in the selected checkout.

| Repository | Owns |
| --- | --- |
| [EmberBSD](https://github.com/oxtech-ember/EmberBSD) | OS, drivers, board/firmware integration, system builds/checks |
| [EmberBSD-Ports](https://github.com/oxtech-ember/EmberBSD-Ports) | Third-party recipes, hashes, patches, pkgsrc overlays and dependency profiles |
| [EmberBSD-Examples](https://github.com/oxtech-ember/EmberBSD-Examples) | Standalone applications and reproducible demonstrations |
| [EmberBSD-Runtime](https://github.com/oxtech-ember/EmberBSD-Runtime) | Application installation, execution, lifecycle and shared device operations |
| [EmberBSD-SDK](https://github.com/oxtech-ember/EmberBSD-SDK) | Application API/ABI, package contracts, developer tools/checks |
| [Ember-Agent-Skills](https://github.com/oxtech-ember/Ember-Agent-Skills) | Developer AI instructions, adapters and skill packaging |
| [EmberBSD-User-Skills](https://github.com/oxtech-ember/EmberBSD-User-Skills) | Operations, diagnostics, personal Ports and GitHub workflows |

Find an existing checkout first. Inspect tracked files and relevant definitions:

```sh
git -C "$repo" ls-files
rg -n "$interface_or_command" "$repo"
```

SDK/Runtime currently contain design documents; verify source/releases before
calling an API. Project names do not imply an `ember` CLI or hardware MCP server.
Neither skills package implements an on-device agent. Agent Plugins distributes
AI skills; a proposed Wasm application catalog is a separate SDK/Runtime contract.
Use public project sources; a private wiki is not a prerequisite for these skills.
