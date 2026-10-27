# Update Ports with a coding agent

Use the [Ports update procedure](https://github.com/oxtech-ember/EmberBSD-Ports/blob/main/docs/update-ports.md).
Use the [SDK planner](https://github.com/oxtech-ember/EmberBSD-SDK/blob/main/docs/ports-plan.md) for graph and result contracts.
Apply the [shared dependency and contribution rules](shared-dependencies.md).
The development environment coordinates the work.
These Python tools do not call an LLM or replace pkgsrc.

1. Identify the requested package set and target ABI.
2. Save the baseline graph before changing recipes.
3. Check current releases across direct, transitive, and build dependencies before adapting their shared recipes.
4. Export evaluated candidate metadata with the Ports collector.
5. Compare locks with the SDK planner.
6. Run existing producers for ready nodes with the selected shared toolchain.
7. Record explicit outcomes, logs, and output hashes.
8. Inspect failures and repair the responsible shared recipe or consumer.
9. Update the package revision when a patch changes its output.
10. Review and test each repair before publication.
11. Export changed inputs and make a new plan after each repair.
12. Continue until the requested closure has the required evidence.
13. Submit tested shared repairs through the authorized contribution channel.

Keep host tools and target packages in separate graph nodes.
Use pkgsrc to evaluate dependencies and match versions.
Preserve baseline locks and failed results.
Verify unchanged artifacts before reuse.
Never record an old file as success after a failed producer.
Do not weaken tests or introduce legacy dependencies to clear failures.
Report artifact completion separately from installed behavior and hardware checks.
Report an unsubmitted repair explicitly when publication is not authorized.

For a release, follow the [SDK release procedure](https://github.com/oxtech-ember/EmberBSD-SDK/blob/main/docs/release-tags.md).
Prepare the source `EMBER_VERSION` and source manifest before building.
Finalize tags only after successful builds and the release checks.
Tag creation and publication need a direct request from the user.
Never update the source version after testing and tag the older output.
