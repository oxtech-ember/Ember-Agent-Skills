# Reuse dependencies and contribute repairs

Read the [Ports update contract](https://github.com/oxtech-ember/EmberBSD-Ports/blob/main/docs/update-ports.md).
Inspect current Ports sources and existing pull requests before creating another recipe or repair.
Preserve local changes when updating the checkout.

## Keep behavior at its common owner

Assign protocol and state-machine policy to existing common owners.
Drivers translate hardware/vendor interfaces and expose offload through common contracts.
Extend missing APIs, adapt consumers, remove duplicate policy, then add the adapter.
Test common regressions and the hardware boundary.

## One shared dependency

Check direct, transitive, build, and test dependencies in the requested closure against current stable upstream releases.
Use a justified supported LTS when required, with current fixes.
Treat old pins and consumer requirements as migration work; adapt consumers to the common version.

Reuse the canonical Ports recipe, source pin, hashes, and complete patch set.
Reuse a package when its [input key](https://github.com/oxtech-ember/EmberBSD-SDK/blob/main/docs/input-keys.md) matches.
The key contains the Ports tree hash, configuration, compiler key, ABI, and target.
Reuse the recorded Git hash or input key as the input identity.
Keep host and target artifacts separate without maintaining different dependency versions for each application or board.
Replace bundled shared-library copies and private dependency downloads with the common Ports dependency.
Repair missing consumer build support while preserving required upstream functionality.
Keep base-library integration in OS while consuming the common Ports sources.

## Repair once

Move diagnostic edits from extracted sources, caches, or sysroots into the owning recipe or source repository.
Keep the regression with that implementation.
Keep one patch at its owner; route applications, profiles, SDK scripts, and skills to that implementation.
Include affected direct and transitive consumers when updating the graph.
Change a consumer revision only when its installed files change.
Remove replaced versions from the active graph after their consumers pass.
After concurrent changes, the merged Git tree gives a new input key.
Rebuild and test the affected consumers for that key.
A conflict-free text merge does not prove compatibility.

Verify the normal build from a clean source revision with documented prerequisites.
Make the documented checkout and prerequisites sufficient for the normal build.
Retain matching evidence when publication does not change the tested inputs.

## Offer the shared repair

EmberBSD welcomes pull requests from users without upstream write access.
Separate the reusable repair from personal application behavior and private material.
Prepare a focused patch and its evidence for the correct public owner.
Use `emberbsd-contribute` or the [public contribution procedure](https://github.com/oxtech-ember/EmberBSD/blob/main/CONTRIBUTING.md).
When publication is authorized, push a topic branch to an authorized repository or fork and open the matching PR.
Reuse existing authorization within its granted scope.
Otherwise, show the prepared diff and checks before asking permission to publish.
If permission is declined, preserve the local patch and report that it remains unsubmitted.
Keep the declined submission local until the user changes that decision.
Skill installation does not grant upstream write or merge permission.
Push upstream `main` only with explicit authorization for that repository and action.
Report prepared, submitted, merged, and released states separately.
Report a local repair as local and an open PR as pending.
