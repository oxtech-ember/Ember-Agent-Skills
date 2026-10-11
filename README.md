# Ember Agent Skills

Task-specific instructions for AI agents working on [EmberBSD](https://github.com/oxtech-ember/EmberBSD).
The package uses [Agent Plugins](https://agent-plugins.org/) and [Agent Skills](https://agentskills.io/specification).
Version **0.4.0** contains eight independently installable skills.

| Skill | Task |
| --- | --- |
| [`emberbsd-repository-guide`](skills/emberbsd-repository-guide/SKILL.md) | Select a repository and task skill when ownership is unclear |
| [`emberbsd-develop-app`](skills/emberbsd-develop-app/SKILL.md) | Create or develop an application or public example using verified interfaces |
| [`emberbsd-build-kernel`](skills/emberbsd-build-kernel/SKILL.md) | Prepare GCC16 tools and cross-build a kernel without an application sysroot |
| [`emberbsd-port-software`](skills/emberbsd-port-software/SKILL.md) | Repair shared recipes and test dependencies and installed consumers |
| [`emberbsd-add-board`](skills/emberbsd-add-board/SKILL.md) | Integrate board build and boot support with measured hardware evidence |
| [`emberbsd-build-static-base`](skills/emberbsd-build-static-base/SKILL.md) | Build and inspect a static base set |
| [`emberbsd-contribute`](skills/emberbsd-contribute/SKILL.md) | Submit an authorized shared change through the accepted channel |
| [`emberbsd-maintain-skills`](skills/emberbsd-maintain-skills/SKILL.md) | Maintain AI instructions, task boundaries, and client metadata |

Each entry has a narrow task description and its own references, client metadata,
and icon. The old repository-guide name remains a short selector. Its previous
reference paths remain as small migration notes. No skill requires sibling files.
Descriptions and procedures use simplified English in the style of ASD-STE100.
See the [authoring rules](docs/skill-writing.md) for limits and verification boundaries.

## Purpose and related projects

Use the [repository map](skills/emberbsd-repository-guide/references/repositories.md)
to locate the owning public source. OS builds and drivers belong to EmberBSD.
Third-party recipes belong to Ports. Public demonstrations belong to Examples.
SDK and Runtime currently contain design documents; verify implemented interfaces
before calling them. This package contains no MCP server or device runtime.

[EmberBSD-User-Skills](https://github.com/oxtech-ember/EmberBSD-User-Skills) handles
operation, installation, diagnostics, personal application changes, and user GitHub work.
Editing an existing program for personal use does not require a contribution PR.
Independent applications keep their own conventions, language, license, and publication scope.
Root `AGENTS.md` governs this plugin repository. Do not copy it over application instructions.

## Add your board

Start with `emberbsd-add-board`, the [board catalog](https://github.com/oxtech-ember/EmberBSD/tree/main/ember/boards),
and the [OS board procedure](https://github.com/oxtech-ember/EmberBSD/blob/main/ember/boards/adding-a-board.md).
Supply the model, revision, SoC, firmware, serial console, and available hardware access.
The workflow covers kernel, DTS/ACPI, drivers, output bundles, boot selection, and evidence.
Keep build, VM, and physical checks separate. A shared SoC does not prove peripheral support.
An authorized shared change includes the board page and a concise catalog row.

## Use in your development environment

Install the repository root with a client that supports Agent Plugins and skills.
Select the `emberbsd-development` plugin. Follow that client's documented Git,
directory, or archive installation method.

For standalone Agent Skills, install the complete `skills/<name>/` directory.
Keep its references, `agents/`, and assets together. Retain the MIT notice.
For manual use, ask the agent to read the selected `SKILL.md` and required references.
Manual reading does not register automatic discovery.

Verify that the client lists all eight task names. For example:

> Use emberbsd-build-kernel to cross-build my AArch64 EmberBSD kernel with GCC16 on host and target.

> Use emberbsd-develop-app to create a UART decoder in my application repository and test synthetic input.

Use the client's explicit selector when available. `$skill-name` is client syntax,
not a requirement of the portable format. Refresh the installed copy through that
client and verify its version after updates.

### Install in Codex

The [Codex guide](docs/codex.md) explains marketplace commands and icon path bases.

```sh
codex plugin marketplace add oxtech-ember/Ember-Agent-Skills --ref main
codex plugin list --marketplace ember-agent-skills --available --json
codex plugin add emberbsd-development@ember-agent-skills
```

These commands use the selected Git ref. An unmerged candidate requires its topic
ref or a local test marketplace; `main` does not include draft changes.

### Install in ZCode and Claude Code

Both clients use `.claude-plugin/marketplace.json`. In ZCode, add
`oxtech-ember/Ember-Agent-Skills` in **Settings → Plugin Management → Discover**
and install **emberbsd-development**. In Claude Code:

```text
/plugin marketplace add oxtech-ember/Ember-Agent-Skills
/plugin install emberbsd-development@ember-agent-skills
```

The catalog points to the repository root. The Claude plugin manifest exposes `skills/`.
The root `plugin.json` remains the canonical portable manifest.

## Package structure

```text
plugin.json                       Portable manifest and OpenAI plugin metadata
.agents/plugins/marketplace.json  Codex catalog
.claude-plugin/                   ZCode and Claude Code adapters
assets/emberbsd-logo.png          Plugin icon
skills/<name>/SKILL.md            One task and its discovery condition
skills/<name>/references/         Only that task's bundled instructions
skills/<name>/agents/openai.yaml  Codex skill presentation
skills/<name>/assets/             Standalone skill icon
scripts/check-package.rb         Package, prose, link, and optional native checks
scripts/test-check-package.rb    Validation regressions
docs/skill-writing.md             Task boundaries and simplified English rules
docs/packaging.md                 Packaging and behavior scenarios
docs/codex.md                     Codex commands and evidence
```

The AI plugin marketplace distributes agent skills. A proposed EmberBSD Wasm
application catalog is a separate SDK/Runtime contract.

## Validate a checkout

Use Ruby with its standard library:

```sh
ruby scripts/test-check-package.rb
ruby scripts/check-package.rb
ruby scripts/check-package.rb --codex
```

The last command requires Codex. It uses temporary profiles and reads native
plugin and skill icon paths without changing saved client settings.
The checks enforce prose limits and skill-local links. They do not certify the
full ASD-STE100 dictionary or prove assistant behavior, device support, or desktop rendering.
Version **0.4.0** passed local consistency, 21 validation regressions, native Codex
discovery, and all plugin/skill icon paths with **Codex CLI 0.159.2** on **2026-10-11**.
All eight folders also passed isolated reference, metadata, icon, and prose checks.

Review the [manual scenarios](docs/packaging.md#checks-and-evidence) after behavior changes.

## License

[MIT](LICENSE).
