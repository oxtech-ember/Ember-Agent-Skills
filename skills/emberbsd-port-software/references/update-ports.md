# Update Ports with a coding agent

Use the [Ports update procedure](https://github.com/oxtech-ember/EmberBSD-Ports/blob/main/docs/update-ports.md).
Use the [SDK planner](https://github.com/oxtech-ember/EmberBSD-SDK/blob/main/docs/ports-plan.md) for graph and result contracts.
The development environment coordinates the work.
These Python tools do not call an LLM or replace pkgsrc.

1. Identify the requested package set and target ABI.
2. Save the baseline graph before changing recipes.
3. Select supported upstream releases and verify their sources.
4. Export evaluated candidate metadata with the Ports collector.
5. Compare locks with the SDK planner.
6. Run existing producers for ready nodes with the shared GCC16 toolchain.
7. Record explicit outcomes, logs, and output hashes.
8. Inspect failures and repair the responsible shared recipe or consumer.
9. Update the package revision when a patch changes its output.
10. Review and test each repair before publication.
11. Export changed inputs and make a new plan after each repair.
12. Continue until the requested closure has the required evidence.

Keep host tools and target packages in separate graph nodes.
Use pkgsrc to evaluate dependencies and match versions.
Preserve baseline locks and failed results.
Verify unchanged artifacts before reuse.
Never record an old file as success after a failed producer.
Do not weaken tests or introduce legacy dependencies to clear failures.
Report artifact completion separately from installed behavior and hardware checks.
