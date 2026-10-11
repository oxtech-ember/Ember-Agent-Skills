---
name: emberbsd-repository-guide
description: "Guide EmberBSD application development, board bring-up, shared ports, dependency upgrades and tested contributions. Use when developing an application, changing the OS or an ecosystem component, adding a board, contributing a shared fix or checking a development support claim. For device operation, application configuration or personal Ports customization of an existing program, use EmberBSD-User-Skills instead."
---

# EmberBSD repository guide

Establish where a change belongs and what the current sources actually support.
Use this guide before selecting an EmberBSD build command, API, or example.

Assist EmberBSD developers and external contributors through available CLI/API
tools. Preserve the user's project instructions and actual permissions.
For an application in the user's own repository, read
[developing applications](references/developing-applications.md). Keep its code
there; route reusable fixes and ports to the owning EmberBSD repository.

Routine device operation and personal customization of an existing program
belong to [EmberBSD-User-Skills](https://github.com/oxtech-ember/EmberBSD-User-Skills).
Source edits and compilation alone do not turn a personal Ports task into a
shared contribution. Keep that user's patch workflow separate; apply this
package's contribution process only to the contribution actually requested.

## Locate the owner

Read [the repository map](references/repositories.md). Respect an explicitly
selected repository, and explain any dependency that belongs elsewhere.

Find an existing checkout before cloning. Inspect its remote, branch, revision,
and uncommitted changes. Read its applicable `AGENTS.md`, README, and documentation
for the requested subsystem. Preserve unrelated work.
Synchronize the working branch with a normal pull when configured; resolve
conflicts without discarding another contributor's changes.

Do not assume these skill files live in the user's working repository. Resolve
bundled references relative to this `SKILL.md`; resolve project paths against the
identified checkout.

## Establish the supported workflow

1. Find the actual API definitions, build commands, examples, and tests in that
   checkout. Cite their paths and the inspected revision when reporting support.
2. Treat the repository map as intended ownership. A named repository does not
   establish that its planned component has been implemented or released.
3. If the SDK or Runtime lacks the required interface, report that gap and work
   from available sources. Do not invent commands, imports, package formats,
   hardware MCP tools, or compatible version ranges.
4. For cross-repository changes, identify the shared contract and its owner.
   Keep ABI definitions and build tools with their owning project; call them
   from skills instead of maintaining alternative implementations here.
5. For compiler/cross work, use the
   [Ports CLI selection](references/ports.md#select-host-and-target-compilers).
   Verify host/target/runtime identities; choose kernel or application mode.

## Make and validate the change

Follow the target project's conventions and task authorization. Contributions
to public EmberBSD repositories use English in source, documentation, comments,
and commit messages. Preserve upstream licenses and attribution. Use NetBSD
KNF for C where required by the target. New EmberBSD utilities, tests, and
examples must not introduce Python; account honestly for existing upstream
dependencies. Independently owned applications retain their own conventions.

For a port or dependency upgrade, read [the Ports workflow](references/ports.md).
Use current stable upstream tools and repair incompatibilities through Ports.
The age of a pkgsrc snapshot does not set EmberBSD's target version. Keep one
coherent dependency set and rebuild affected consumers instead of hiding ABI
failures behind library symlinks or a permanent old version per application.

For a new board, platform adaptation or hardware-validation contribution, read
[adding boards](references/adding-boards.md). Use the OS's board catalog and
contribution guide; include boot/build integration and evidence for each claimed
interface. Shared silicon is not proof of a second board's support.

For a fully static userland or fixed image, read
[static builds](references/static-builds.md). Use the verified flag set and the
race catalog there instead of rediscovering them; state the real trade-offs —
static linking does not speed up boot.

Choose checks that demonstrate the requested behavior. Distinguish inspected
source, a successful build, contract tests, a VM boot, and a physical board test.
For hardware claims, record the board, firmware, configuration, test conditions,
and unverified components. Compilation alone does not establish device support.
For a bug fix, retain a regression that detects its cause and show failure before
the fix and success after it. Run checks appropriate to the change; do not repeat
a full suite after it passes without a new failure, change, or unresolved concern.

Use the user's authorized scope for commits, publication, and deployment.
A request to write an application does not by itself request flashing a board.
Public examples and reports must work without private configuration or secrets.

## Contribute and preserve the lesson

For an authorized contribution, after relevant tests pass, open a focused PR
from a contribution branch for the completed fix or port in its owning EmberBSD
repository. Do not treat ordinary application development as permission to
publish the user's project. Prepare reusable upstream changes too; submit them
when the task authorizes that destination, following
[the contribution workflow](references/contributions.md).
Use the accepting project's real submission channel and current AI/provenance
rules; a GitHub mirror is not necessarily a PR destination. Do not auto-merge.
Honor explicit task-specific publication instructions and the host's permissions.

Update the affected build instructions and this skill's relevant reference when
a verified result changes a reusable rule or workaround. Record the source,
tested revision, affected versions, and condition for removing the workaround.
Replace obsolete guidance; do not turn a temporary observation into a universal
ban. See [maintaining this guidance](references/maintenance.md).

Report the owning repository, changes or findings, checks actually run,
remaining gaps, and PR/submission links with their actual status. If a required
checkout or tool is unavailable, state the exact limitation rather than
implying that validation passed.
