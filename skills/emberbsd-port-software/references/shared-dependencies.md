# Reuse dependencies and contribute repairs

Read the [Ports update contract](https://github.com/oxtech-ember/EmberBSD-Ports/blob/main/docs/update-ports.md).
Inspect current Ports sources and existing pull requests before creating another recipe or repair.
Preserve local changes when updating the checkout.

## One shared dependency

Check versions for direct, transitive, build, and test dependencies in the requested closure.
Select current stable upstream or a justified supported LTS with current fixes.
An old pkgsrc pin or consumer requirement does not justify another legacy version.
Update or adapt consumers to the common version.

Reuse the canonical Ports recipe, source pin, hashes, and complete patch set.
Reuse a package when its [input key](https://github.com/oxtech-ember/EmberBSD-SDK/blob/main/docs/input-keys.md) matches.
The key contains the Ports tree hash, configuration, compiler key, ABI, and target.
Do not add checks that reread or rehash inputs that a git hash or input key already identifies.
Keep host and target artifacts separate without maintaining different dependency versions for each application or board.
Replace bundled shared-library copies and private dependency downloads with the common Ports dependency.
Repair missing consumer build support while preserving required upstream functionality.
Keep base-library integration in OS while consuming the common Ports sources.

## Repair once

Move diagnostic edits from extracted sources, caches, or sysroots into the owning recipe or source repository.
Keep the regression with that implementation.
Do not copy the same patch into applications, profiles, SDK scripts, or skills.
Include affected direct and transitive consumers when updating the graph and package revisions.
Remove replaced versions from the active graph after their consumers pass.
After concurrent changes, the merged Git tree gives a new input key.
Rebuild and test the affected consumers for that key.
A conflict-free text merge does not prove compatibility.

Verify the normal build from a clean source revision with documented prerequisites.
Do not require hidden local files or manual patching after checkout.
Retain matching evidence when publication does not change the tested inputs.

## Offer the shared repair

EmberBSD welcomes pull requests from users without upstream write access.
Separate the reusable repair from personal application behavior and private material.
Prepare a focused patch and its evidence for the correct public owner.
Use `emberbsd-contribute` or the [public contribution procedure](https://github.com/oxtech-ember/EmberBSD/blob/main/CONTRIBUTING.md).
When publication is authorized, push a topic branch to an authorized repository or fork and open the matching PR.
Existing authorization remains valid; do not request it again.
Otherwise, show the prepared diff and checks before asking permission to publish.
If permission is declined, preserve the local patch and report that it remains unsubmitted.
Do not repeat a declined publication request.
Skill installation does not grant upstream write or merge permission.
Do not push upstream `main` merely because the user can build EmberBSD.
Report prepared, submitted, merged, and released states separately.
Do not describe a local repair or pending PR as available to all users.
