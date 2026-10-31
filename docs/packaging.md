# Portable packaging and validation

The canonical format is [Agent Plugins 1.0.0](https://agent-plugins.org/specification).
Skills follow the [Agent Skills specification](https://agentskills.io/specification).
These primary references were checked on **2026-10-08**.

## Package and client boundaries

`plugin.json` identifies `emberbsd-development`; its `$schema` declares the
Agent Plugins format version. The package's release version is a separate
field. Each of the nine task skills lives in `skills/<name>/`.
Each directory contains its own `SKILL.md`, references, metadata, and icon.
The legacy repository guide is a short selector.

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
| `.grok-plugin/marketplace.json` | Catalog for the Grok Build marketplace loader; clones the repository URL |
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
Install or refresh from these canonical sources. Preserve users' application instructions.
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
references using Ruby's standard library. It checks all bundled Markdown links
inside each owning skill, including deep references, and enforces the prose limits
in [the authoring rules](skill-writing.md). Run `ruby scripts/test-check-package.rb`
for negative fixtures and parser regressions. It is a consistency check, not a full implementation
of either specification's validator.

When Codex is available, also run `ruby scripts/check-package.rb --codex` and
record `codex --version`. This uses a temporary profile and command-line
marketplace configuration, so an installed release cannot mask the candidate.
It also checks native plugin and skill icon paths through an isolated app-server
`plugin/read` request. It does not register or install the package in saved settings
or prove desktop icon rendering.
When Grok Build is available, also run `ruby scripts/check-package.rb --grok`
and record `grok --version`. It uses a temporary `GROK_HOME` and a local copy
of the Grok catalog that clones this checkout. Commit the candidate first.
Grok installs the committed `HEAD`, not uncommitted files. The check compares
the installed version and the skills that `grok inspect --json` loads.
The [Codex guide](codex.md) describes that adapter. Record equivalent evidence
before claiming another client's installation or behavior has been tested.

Select the narrow skill directly from its description. Do not require the
repository selector first. Install one complete skill directory in isolation
and verify that its links, metadata, and icon remain usable.

After installing in a test environment, exercise these skill scenarios:

| Prompt or situation | Expected behavior |
| --- | --- |
| Inspect or create a workspace before acquiring the SDK | Use an installed Python accepted by the command; do not require a completed build tool set |
| Acquire native tools before cross-building | Build the native Clang/LLVM prefix from common Ports recipes, then build the cross SDK |
| System `cc` is Apple Clang while a native SDK prefix is selected | Reject ordinary fallback; use the prefix compiler. Declared initial bootstrap remains separate |
| `HOST_CC` points to the selected compiler but SDK resolves `cc` again | Inspect the real plan and stop the dependent build; repair the common selector |
| SDK lacks a native compiler, generator, or build interpreter | Repair the SDK/Ports provider; do not install a system substitute or hide it behind a local wrapper |
| The SDK cross compiler is offered for a native generator | Reject the host/target mismatch; select a host-executable native compiler |
| CMake, Meson, configure, or a nested make retains a system tool | Reject stale selection; update the owning producer and invalidate incompatible cached outputs |
| A system binary is symlinked into the SDK | Resolve the symlink and reject the build tool outside the selected prefix |
| Native tools require host system ABI headers or libraries | Allow these native inputs; keep them outside target searches |
| The sysroot launcher runs with an external control Python | Pass `--host-prefix`; let SDK select its build Python without forcing the launcher's interpreter |
| A legacy bootstrap profile names GCC14 | Use the current Ports bootstrap procedure. Use Clang/LLVM by default and an explicit GCC platform profile when needed. |
| Clang Static Analyzer or a diagnostic fuzz target is requested | Separate diagnostic outputs from production; replay fuzz inputs with the selected production compiler and runtime |
| Cross-build a kernel without an application sysroot | Select `emberbsd-build-kernel`; load its own references only |
| Create a new application | Select `emberbsd-develop-app`; keep independent application conventions |
| Build a static base set | Select `emberbsd-build-static-base`; require complete tools and runtime |
| Edit AI discovery descriptions or icons | Select `emberbsd-maintain-skills`; check all standalone bundles |
| Operate a device or customize an existing app in personal Ports | Route to EmberBSD-User-Skills; do not require a contribution merely because source editing is involved |
| Build an application in a user's own repository | Read its conventions, reuse real public interfaces/examples, and keep application code in that repository |
| A private application discovers a reusable EmberBSD bug | Isolate the minimal fix; preserve private material and obtain publication permission if it is outside the task |
| A shared dependency recipe already exists under `pkgsrc/` | Reuse that recipe and its complete patch set; do not search only profiles and probes |
| An application bundles an old dependency or downloads another private copy | Adapt its build to the current Ports dependency; check affected consumers instead of preserving a separate old stack |
| A patch exists only in extracted sources or a sysroot | Move it into the owning recipe with a regression; verify a clean normal build without hidden local inputs |
| A user authorized a tested shared repair and its PR | Complete the authorized fork or topic-branch submission; do not stop at a local commit or request permission again |
| A private application repair lacks publication permission | Prepare the public-owner diff and tests without private material, then request permission; do not push first |
| A user declines publication of a prepared shared repair | Preserve the patch locally and report it as unsubmitted; do not repeat the request or claim a public fix |
| Another contributor updates the same dependency | The merged Git tree gives a new input key; rebuild and test affected consumers. A text merge alone does not prove compatibility |
| An agent wants to recheck inputs before reuse | Reuse when the [input key](https://github.com/oxtech-ember/EmberBSD-SDK/blob/main/docs/input-keys.md) matches. Do not add checks that reread or rehash inputs that a git hash or input key already identifies. |
| A fix corrects step order, a typo, a path, or a similar mechanical error | Add no regression test; such a test costs time and adds no value. A logic or behavior fix still needs a causal regression test |
| A shared repair has an open PR but no merge or release | Report the PR URL and pending state; do not claim availability to all users |
| Contribute a tested port without upstream write access | Use a topic branch in a fork and open a PR against the correct target/base; never assume permission to push upstream main |
| An independent application uses a different language or license | Preserve its choices; apply EmberBSD contribution conventions only to changes offered to EmberBSD repositories |
| Add a standalone UART decoder demonstration | Inspect Examples and any required OS/SDK interfaces; identify actual build checks |
| Request an SDK command that is absent from the checkout | Report the missing interface without inventing a command or ABI |
| Claim board support based only on a successful build | Distinguish compilation from VM and physical device evidence |
| Add a board with the same SoC as an existing platform | Read the board contribution reference, inspect wiring/firmware differences, integrate boot/build outputs, and record only tested interfaces |
| A new board builds but the contributor has no hardware | Preserve useful source/build results, state the missing device validation, and avoid a physical-support claim |
| A tested board contribution is ready | Update the canonical DevBoards profile and support limits; keep OS code, builder contracts and checks beside their implementation |
| Invoke the installed skill from a different working directory | Read its bundled repository map from the plugin location |
| pkgsrc carries an older compiler or runtime | Verify current upstream, repair compatibility in Ports and test the affected dependency closure |
| A Linux host has GCC14 but a kernel cross build is requested without a userland sysroot | Verify host and target tools separately, select the Clang/LLVM prefix or an explicit GCC platform profile, and derive sysroot requirements from the kernel artifact |
| A shared compiler prerequisite needs a compatibility repair | Fix the owning Ports recipe, retain its tests and use the corrected helper rather than copying a workaround into skills |
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
| A C/C++ port adds a memory warning | Compare pinned upstream and patched findings with the same target settings; repair the cause with a regression |
| A Cppcheck run uses host headers for an EmberBSD target | Correct the compilation database, target ABI, macros and includes before interpreting the result |
| Valgrind is unavailable for the host or target | Record the exact support gap and alternative memory checks; never report a Valgrind pass |
| Research a custom carrier using DevBoards | Read the exact carrier and board sources; check design transfer assumptions and keep implementation checks in OS/Ports |
| Find shared release orchestration in OS | Route its implementation and contracts to SDK; retain OS source build rules with their subsystem |
| Find a standalone desktop application in OS | Keep it in Examples or its own repository; keep dependency recipes in Ports |
| Find hardware descriptions in OS image documentation | Move hardware applicability and boot layouts to DevBoards; retain image builder mechanics and software contracts in OS |
| Record a new physical support result | Update the current DevBoards scenario and limits with provenance; do not append a test diary or duplicate catalog |
| A related board has a different bootloader | Follow the selected board's loader contract; do not infer its image format from the SoC |
| A kernel driver passes a user-space memory model | Keep native kernel, DMA, concurrency and hardware acceptance separate |
| An analyzer warns in imported code | Record ownership and impact; justify only narrow suppressions and retain unsuppressed new defects |
| Upstream removes the reason for a workaround | Retest and remove obsolete patch/guidance; preserve the source and acceptance state |
| Upgrade a shared dependency across an API or ABI change | Map used changes to consumers; complete one pilot before migrating the dependency closure |
| The old release cannot run and trusted output is missing | Use independent target expectations; leave historical equivalence unverified without installing obsolete tools |
| A migration check always reports success | Break a disposable candidate and alter a captured output byte; require both checks to detect the fault |
| A small target VM is used for cross-build acceptance | Size compilation from host resources and target execution from guest resources |
| A security repair intentionally changes malformed-input behavior | Test the supported contract and document the difference; do not restore the old defect |

These are manual acceptance scenarios. Package discovery alone does not prove
that an assistant will satisfy them or improve over an unassisted baseline.

On **2026-10-11**, version **0.4.1** passed local consistency and all 21 validator
regressions. **Codex CLI 0.159.2** discovered all eight skills and resolved every
plugin and skill icon path. Eight isolated folders passed local reference,
metadata, icon, and prose checks; all ten bundled shell blocks parsed with `sh -n`.
All entries remain below the 250-word prose limit.

Read-only source review used OS `d472eb8fecc3ff70b6aa231888b301414985845c` and
Ports `19ca1d49aae3f6775bba27390aac948e5e277039`. The kernel recipe accepts
`--kernel` without an application sysroot. The OS builder requires an absolute
output directory outside its source tree. These source checks do not rerun the
compiler or establish target execution. Desktop rendering remains untested.

Maintain the reusable rules in the skill's bundled
[maintenance reference](../skills/emberbsd-maintain-skills/references/skill-changes.md).
Update commands and compatibility cases when a verified change invalidates them.
Do not copy machine-local build logs, private network addresses or credentials
into published examples or prompts.


## SDK tool selection acceptance

The [SDK policy](https://github.com/oxtech-ember/EmberBSD-SDK/blob/main/docs/tool-selection.md)
owns acquisition, native prefix selection, and build checks.
Review the scenarios above for the native/target distinction, prefix containment,
host CPU compatibility, host ABI inputs, diagnostic exceptions, and publication scope.
Acquisition and workspace commands do not need a separately qualified SDK or acceptance receipt.

Run `python3 -B skills/emberbsd-prebuild-sdk/tests/test_launcher.py` for launcher transport checks.
These cover workspace commands without a build Python version gate, explicit source selection,
native-prefix forwarding, optional Python aliases, and standalone installation.
Package checks and launcher fixtures do not establish a complete SDK build or general assistant reliability.

## Shared dependency contribution acceptance

On **2026-10-24**, version **0.4.18** passed local consistency and all 24 validator regressions
with Ruby **4.0.8** on macOS arm64. All nine standalone bundles passed their local reference,
prose, metadata, and icon checks. Their files matched the final skill sources.
Codex CLI **0.163.0-alpha.11.2** discovered all nine skills and resolved plugin and skill icons.
Grok Build **1.0.62** installed the committed candidate and loaded all nine skills in an isolated profile.

Independent read-only review exercised four textual scenarios: an existing shared dependency,
an authorized fork PR, missing publication permission, and an explicit refusal.
The review checked owner selection, private application boundaries, and accurate submission states.
These bounded checks do not establish actual agent execution, downstream builds, or PR acceptance.
No user application or contribution was published by the scenario checks.

## Current port guidance acceptance

On **2026-10-15**, version **0.4.4** passed local consistency and all 21 validator regressions.
Codex CLI **0.159.2** discovered all eight skills and resolved plugin/skill icons.
The port skill passed standalone links, metadata, icons, and two shell-block syntax checks.
Its entry has 211 prose words; the new modernization reference has 404.
The CLI comparison accepted identical captures and rejected changed stdout, stderr, and status.

The instruction trial used one repeated scenario: upgrade a shared codec with no runnable baseline,
an empty CTest suite, old staged binaries, a 2 GiB execution VM, and deadline pressure.
Five no-skill controls and one original-skill response omitted the output-byte comparator check
and sized compilation from guest RAM. All five updated-skill responses required both fault
controls, separated host/guest budgets, and left historical equivalence unverified.
These are fresh-context response trials, not executed port migrations or a statistical benchmark.
The source method is linked from the skill's modernization reference; no external plugin or scripts are required.
Desktop rendering, downstream memory safety, and hardware acceptance remain outside these checks.

## DevBoards routing acceptance

On **2026-10-15**, version **0.4.5** passed local consistency and all 21 validator regressions with Ruby **4.0.7**.
Codex CLI **0.162.0-alpha.17.2** discovered all 8 skills and resolved plugin and skill icon paths.
All 8 folders passed isolated reference, prose, metadata, icon, and license checks.
DevBoards was publicly readable at revision `f4a6410ee770d7c47ef64d5bb2618ca7e271347f`.
Source review checked the catalog, reader guide, layer ownership, and configuration applicability.
This verifies instruction routing and packaging; it does not establish agent execution or hardware support.

## Kimi Code manifest packaging

On **2026-10-16**, version **0.4.6** passed local consistency and all 22 validator regressions with Ruby **4.0.7**.
The new `kimi.plugin.json` follows the documented Kimi Code plugin schema:
required `name` and `version`, display `interface` fields, and `skills` at `./skills/`.
The validator now rejects identity, version, description, license, skills-path, and interface
disagreements between the Kimi manifest and the portable manifest.
This verifies packaging only. Installation and skill loading in the Kimi Code client were not executed in this check.

## Prebuild SDK routing

Version **0.4.7** adds `emberbsd-prebuild-sdk` and SDK/sysroot routing.
Local consistency and all 22 validator regressions pass. Codex CLI
**0.163.0-alpha.10.2** discovers all nine skills in an isolated profile and
resolves the native plugin and skill icon paths. These checks ran on macOS
arm64 with Ruby **4.0.7**.

The new entry and reference keep workspace layout, sysroot build, package
closure and target execution separate. They route executable work to
EmberBSD-SDK, OS and Ports, and remain usable as a standalone skill directory.
Its bundled Python launcher passes seven transport contracts under CPython
**3.15.0** with `-B -I -S`. The tests check literal argv, interpreter identity,
source selection, command containment, child failure and a copied standalone script.
Read-only inspection of an existing adopted workspace and sysroot help also
pass through the actual SDK commands. No additional workspace is created.
These packaging checks do not establish assistant behavior, an accepted
sysroot build, Windows support or a redistributable binary SDK.

## Target workspace routing

Version **0.4.8** selects one workspace for each target architecture.
The canonical layout manifest declares the target and triplet.
An alias name does not declare either value.
The guidance keeps legacy inspection separate from target migration.

Local consistency and all 22 validator regressions pass with Ruby **4.0.7**.
Codex CLI **0.163.0-alpha.10.2** discovers all nine skills in an isolated
profile and resolves plugin and skill icon paths.
All seven launcher contracts pass under CPython **3.15.0** with `-B -I -S`.
These checks ran on macOS arm64.
The actual launcher also passed ten layout invocations and sysroot help against
SDK `51a545b2917d589d2dd58fc0e5e424a9e3cb6d24` from an unrelated directory.
The checks created both target layouts, inspected them, adopted a matching
workspace, and repeated that adoption.
Wrong-target and unknown-target adoption refused without changing the source.
Legacy inspection preserved an unknown target and the existing files.
They do not establish a target sysroot build or native Windows support.

## Grok Build marketplace packaging

On **2026-10-21**, version **0.4.9** passed local consistency and all 24 validator regressions with Ruby **4.0.7**.
Grok Build **1.0.62** reads `.grok-plugin/marketplace.json` before `.claude-plugin/marketplace.json`.
It rejects the `.claude-plugin` entry source `./` with `marketplace path is empty`.
Grok also rejects current-directory components in a catalog path.
The Grok catalog entry therefore uses a `url` source with the repository Git URL.
The entry has no `sha` pin, so an install follows the default branch.
`grok plugin validate` accepts the root `plugin.json`.
The `--grok` check installed the committed candidate in a temporary `GROK_HOME`.
Grok loaded all 9 skills from the plugin.
These checks ran on macOS arm64.
This verifies packaging and skill discovery only. It does not establish assistant behavior.
