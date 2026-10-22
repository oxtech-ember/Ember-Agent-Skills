# Ember Agent Skills

Task-specific instructions for AI agents working on [EmberBSD](https://github.com/oxtech-ember/EmberBSD).
The package uses [Agent Plugins](https://agent-plugins.org/) and [Agent Skills](https://agentskills.io/specification).
Version **0.4.14** contains nine independently installable skills.

| Skill | Task |
| --- | --- |
| [`emberbsd-repository-guide`](skills/emberbsd-repository-guide/SKILL.md) | Select a repository and task skill when ownership is unclear |
| [`emberbsd-prebuild-sdk`](skills/emberbsd-prebuild-sdk/SKILL.md) | Create, inspect and reuse a shared workspace; build the EmberBSD sysroot |
| [`emberbsd-develop-app`](skills/emberbsd-develop-app/SKILL.md) | Create or develop an application or public example using verified interfaces |
| [`emberbsd-build-kernel`](skills/emberbsd-build-kernel/SKILL.md) | Prepare GCC16 tools and cross-build a kernel without an application sysroot |
| [`emberbsd-port-software`](skills/emberbsd-port-software/SKILL.md) | Port or modernize shared software and verify behavior against independent evidence |
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
SDK provides Prebuild SDK workspace tools and sysroot orchestration.
Stable application contracts and Runtime remain separate work. Verify implemented interfaces before calling them. This package contains no MCP server or device runtime.

[EmberBSD-User-Skills](https://github.com/oxtech-ember/EmberBSD-User-Skills) handles
operation, installation, diagnostics, personal application changes, and user GitHub work.
Editing an existing program for personal use does not require a contribution PR.
Independent applications keep their own conventions, language, license, and publication scope.
Keep the application's existing instructions when you install skills.

Development checks cover Cppcheck, GCC and Clang static analysis, and Valgrind Memcheck.
The guidance includes upstream-versus-patch comparisons for ports, justified suppressions,
and explicit platform limits. Kernel contracts and hardware acceptance remain separate.
Version and dependency migrations use a small pilot, explicit behavior contracts,
independent comparisons, and negative controls for the tests and comparator.
The port skill also covers agent-driven updates with the Ports collector and SDK planner.
The tools preserve dependency graphs and result evidence; the development environment coordinates repairs.


## Add your board

Start with `emberbsd-add-board`, the [board catalog](https://github.com/oxtech-ember/EmberBSD/tree/main/ember/boards),
and the [OS board procedure](https://github.com/oxtech-ember/EmberBSD/blob/main/ember/boards/adding-a-board.md).
Supply the model, revision, SoC, firmware, serial console, and available hardware access.
The workflow covers kernel, DTS/ACPI, drivers, output bundles, boot selection, and evidence.
Keep build, VM, and physical checks separate. A shared SoC does not prove peripheral support.
An authorized shared change includes the board page and a concise catalog row.

[EmberBSD-DevBoards](https://github.com/oxtech-ember/EmberBSD-DevBoards) provides hardware references for developers building their own devices.
It separates board, carrier, SoC, interface, and bootloader knowledge.
Start with its [reader guide](https://github.com/oxtech-ember/EmberBSD-DevBoards/blob/main/docs/reader-guide.md) and [catalog](https://github.com/oxtech-ember/EmberBSD-DevBoards/blob/main/catalog.json), then check each profile's sources and applicability.
Drivers, build procedures, and current support evidence remain in their implementation repositories.

## Use in your development environment

Install the repository root with a client that supports Agent Plugins and skills.
Select the `emberbsd-development` plugin. Follow that client's documented Git,
directory, or archive installation method.

For standalone Agent Skills, install the complete `skills/<name>/` directory.
Keep its references, `agents/`, and assets together. Retain the MIT notice.
For manual use, ask the agent to read the selected `SKILL.md` and required references.
Manual reading does not register automatic discovery.

Verify that the client lists all nine task names. For example:

> Use emberbsd-prebuild-sdk to reuse my shared SDK workspace and build the EmberBSD sysroot with GCC16.

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

### Install in Kimi Code

Kimi Code reads `kimi.plugin.json` at the repository root. The manifest exposes `skills/`.
Install from the Plugins screen or run:

```text
/plugins install oxtech-ember/Ember-Agent-Skills
```

A ref can be added to the URL form, for example `oxtech-ember/Ember-Agent-Skills/tree/<ref>`.
Reinstall the plugin after a release; Kimi Code does not update it automatically.

### Install in Grok Build

Grok Build reads `.grok-plugin/marketplace.json`:

```sh
grok plugin marketplace add oxtech-ember/Ember-Agent-Skills
grok plugin install emberbsd-development --trust
grok plugin details emberbsd-development
```

The catalog entry clones this repository from GitHub.
Grok rejects a repository-root path such as `./` in a catalog entry.
To update, run `grok plugin marketplace update` and `grok plugin update emberbsd-development`.

## Package structure

```text
plugin.json                       Portable manifest and OpenAI plugin metadata
.agents/plugins/marketplace.json  Codex catalog
.claude-plugin/                   ZCode and Claude Code adapters
kimi.plugin.json                  Kimi Code adapter
.grok-plugin/marketplace.json     Grok Build catalog
assets/emberbsd-logo.png          Plugin icon
skills/<name>/SKILL.md            One task and its discovery condition
skills/<name>/references/         Only that task's bundled instructions
skills/<name>/agents/openai.yaml  Codex skill presentation
skills/<name>/assets/             Standalone skill icon
scripts/check-package.rb         Package, prose, link, and optional native checks
scripts/test-check-package.rb    Validation regressions
scripts/org-grep                 Search every organization repository and report coverage
scripts/org-grep-test            Offline regressions for org-grep
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
ruby scripts/check-package.rb --grok
```

The `--codex` check requires Codex. It uses temporary profiles and reads native
plugin and skill icon paths without changing saved client settings.
The `--grok` check requires Grok Build. It installs the committed `HEAD` in a temporary `GROK_HOME`.
It checks the installed version and every loaded skill.
The checks enforce prose limits and skill-local links. They do not certify the
full ASD-STE100 dictionary or prove assistant behavior, device support, or desktop rendering.
Version **0.4.4** passed local consistency, all 21 validator regressions, native Codex
discovery, and plugin/skill icon resolution with **Codex CLI 0.159.2** on **2026-10-15**.
The port skill also passed standalone reference/metadata/icon checks and four CLI comparison cases.
Five fresh-context instruction trials included the comparator fault check and correct host resource sizing;
five controls and the original skill omitted those two requirements.
These bounded trials do not establish general assistant reliability or downstream port acceptance.

Version **0.4.5** passed package checks, 21 validator regressions, isolated skill checks, and native Codex discovery on **2026-10-15**.
See the [DevBoards routing checks](docs/packaging.md#devboards-routing-acceptance) for evidence and limits.
Version **0.4.6** added the Kimi Code manifest and passed package checks with 22 validator regressions on **2026-10-16**.
See [Kimi Code manifest packaging](docs/packaging.md#kimi-code-manifest-packaging) for evidence and limits.
Version **0.4.9** added the Grok Build catalog.
See [Grok Build marketplace packaging](docs/packaging.md#grok-build-marketplace-packaging) for evidence and limits.
Current guidance separates target ABIs, shares package objects, and preserves sysroot replacement safety.
Board checks reuse matching stack evidence and cover the device layer.
Shared changes require the affected stack checks.

Review the [manual scenarios](docs/packaging.md#checks-and-evidence) after behavior changes.

## License

[MIT](LICENSE).
