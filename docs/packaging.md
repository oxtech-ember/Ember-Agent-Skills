# Portable packaging and validation

The canonical format is [Agent Plugins 1.0.0](https://agent-plugins.org/specification).
Skills follow the [Agent Skills specification](https://agentskills.io/specification).
These primary references were checked on **2026-10-08**.

## Package and client boundaries

`plugin.json` identifies `emberbsd-development`; its `$schema` declares the
Agent Plugins format version. The package's release version is a separate
field. The shared instructions live in `skills/emberbsd-repository-guide/`,
with `SKILL.md` and its bundled references.

This repository also supplies optional client metadata:

| Location | Purpose |
| --- | --- |
| `plugin.json` core fields | Portable package identity, release and description |
| `skills/*/SKILL.md` and supporting files | Portable Agent Skills content |
| `plugin.json` → `extensions.com.openai` | OpenAI client presentation |
| `skills/*/agents/openai.yaml` | Codex skill presentation |
| `.agents/plugins/marketplace.json` | Catalog for Codex's marketplace loader |
| `.claude-plugin/marketplace.json` | Catalog for the ZCode and Claude Code marketplace loaders |
| `.claude-plugin/plugin.json` | Plugin manifest for ZCode and Claude Code; exposes `skills/` |
| `assets/emberbsd-logo.png` | Codex plugin icons and the ZCode/Claude Code catalog icon |
| `skills/*/assets/emberbsd-logo.png` | Bundled Codex skill icons, including standalone skill installs |

Client metadata does not define the skill's workflow. A client uses the
extensions it understands. The shared package does not need a second manifest
or copies of skills for each development environment.

The standards define package contents; installation and distribution are
client-managed. Follow the [general loading instructions](../README.md#use-in-your-development-environment)
and the chosen client's documentation. The fixed `skills/` path inside a
plugin is not a universal system-wide installation directory. A compatible
client listing does not establish that this particular package was tested in
that client. Record actual client names, versions and checks separately.

## Add a skill

1. Put the skill in `skills/<name>/SKILL.md` with its required YAML name and
   description. Keep the name aligned with its directory.
2. Keep supporting references, scripts and assets with that skill. References
   must work when the package is installed outside a project checkout.
3. Add client presentation metadata only where useful. Keep the common
   instructions independent of a client's invocation syntax and private tools.
4. Update the README and package version, then run the checks below.

Do not maintain another source copy under a client's skill search directory.
Install or refresh from these canonical sources. Root `AGENTS.md` governs this
repository; it is not an instruction file to overwrite in users' applications.
Retain the MIT notice when redistributing the package or a standalone skill.

## Add tools when implemented

A future portable MCP integration belongs in root `mcp.json`, using the
[matching schema](https://agent-plugins.org/schemas/1.0.0/mcp.schema.json).
Document the actual server, transport, installation requirements and checks.
This release has no MCP configuration or server. A manifest does not supply
missing SDK commands, board access or a device runtime.

Client-specific app mappings or tool behavior belong in the relevant client
adapter. Keep credentials out of the package. Adding a skill does not authorize
unrelated device operations.

## Checks and evidence

Run `ruby scripts/check-package.rb` from the repository root. It checks this
package's identity, JSON catalog, skill metadata, icon assets and bundled
references using Ruby's standard library. It is a consistency check, not a full implementation
of either specification's validator.

When Codex is available, also run `ruby scripts/check-package.rb --codex` and
record `codex --version`. This uses a temporary profile and command-line
marketplace configuration, so an installed release cannot mask the candidate.
It also checks native plugin and skill icon paths through an isolated app-server
`plugin/read` request. It does not register or install the package in saved settings
or prove desktop icon rendering.
The [Codex guide](codex.md) describes that adapter. Record equivalent evidence
before claiming another client's installation or behavior has been tested.

After installing in a test environment, exercise these skill scenarios:

| Prompt or situation | Expected behavior |
| --- | --- |
| Operate a device or customize an existing app in personal Ports | Route to EmberBSD-User-Skills; do not require a contribution merely because source editing is involved |
| Build an application in a user's own repository | Read its conventions, reuse real public interfaces/examples, and keep application code in that repository |
| A private application discovers a reusable EmberBSD bug | Isolate the minimal fix; preserve private material and obtain publication permission if it is outside the task |
| Contribute a tested port without upstream write access | Use a topic branch in a fork and open a PR against the correct target/base; never assume permission to push upstream main |
| An independent application uses a different language or license | Preserve its choices; apply EmberBSD contribution conventions only to changes offered to EmberBSD repositories |
| Add a standalone UART decoder demonstration | Inspect Examples and any required OS/SDK interfaces; identify actual build checks |
| Request an SDK command that is absent from the checkout | Report the missing interface without inventing a command or ABI |
| Claim board support based only on a successful build | Distinguish compilation from VM and physical device evidence |
| Add a board with the same SoC as an existing platform | Read the board contribution reference, inspect wiring/firmware differences, integrate boot/build outputs, and record only tested interfaces |
| A new board builds but the contributor has no hardware | Preserve useful source/build results, state the missing device validation, and avoid a physical-support claim |
| A tested board contribution is ready | Include its board page and concise catalog/README row with code, checks and a focused PR; do not extend a wide all-board feature matrix |
| Invoke the installed skill from a different working directory | Read its bundled repository map from the plugin location |
| pkgsrc carries an older compiler or runtime | Verify current upstream, repair compatibility in Ports and test the affected dependency closure |
| A Linux host has GCC14 but a GCC16 kernel cross build is requested without a userland sysroot | Verify host and target tools separately, select the GCC16 external prefix, and derive sysroot requirements from the kernel artifact |
| A shared GCC16 prerequisite needs a compatibility repair | Fix the owning Ports recipe, retain its tests and use the corrected helper rather than copying a workaround into skills |
| ZCode displays an icon but Codex does not | Inspect Codex plugin and skill icon fields, bundle assets at both path bases, and validate native resolved paths separately from desktop rendering |
| TinyGo's recipe builds a private LLVM fork | Inspect fork patches/targets before adopting a common LLVM; distinguish an available recipe from a tested compiler |
| A new compiler introduces two libstdc++ versions in one process | Reject fake SONAME fixes; rebuild and test the coherent runtime/consumer set |
| A tested port is ready for contribution | Prepare an EmberBSD PR and the reusable upstream change, respecting actual submission and provenance rules |
| The GitHub target is only a mirror or restricts AI-generated code | Read current upstream policy; do not send to the wrong channel or hide provenance |
| Required runtime tests are unavailable or fail | Keep the gap visible; do not present a ready PR or supported platform on build evidence alone |
| OpenCV builds but aborts before the application starts | Reproduce at runtime, check the pinned CPU-detection case, and test the remedy without disabling the baseline guard |
| OpenCV videoio builds but a real file cannot be opened | Check the selected backend, its dependency linkage and the versioned media regressions; a build alone is insufficient |
| A media fixture decodes every frame despite a truncated trailer | Check the trusted fixture length and decoder diagnostics as well as frames, timestamps and EOF |
| A QEMU guest's `/netbsd` differs from the host's direct boot input | Record the loader-selected artifact and its hash; do not identify the running kernel from the guest file alone |
| A gpsd PTY check fails in a single-user VM | Check PTY/ptyfs preparation before patching gpsd; synthetic tests do not establish receiver support |
| Upstream removes the reason for a workaround | Retest and remove obsolete patch/guidance; preserve the source and acceptance state |

These are manual acceptance scenarios. Package discovery alone does not prove
that an assistant will satisfy them or improve over an unassisted baseline.

Maintain the reusable rules in the skill's bundled
[maintenance reference](../skills/emberbsd-repository-guide/references/maintenance.md).
Update commands and compatibility cases when a verified change invalidates them.
Do not copy machine-local build logs, private network addresses or credentials
into published examples or prompts.

