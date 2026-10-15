# Modernization checks

## Define the migration

Read the selected upstream release notes and existing Ports patches.
Check whether upstream already fixes the incompatibility.
Record the source revision, target release, compiler, sysroot, flags, and dependency closure.
Map used API, ABI, file-format, and configuration changes to affected consumers.
Keep the existing language and architecture unless the task includes their replacement.
Start with one component and its installed consumer.

Define critical behavior as inputs, expected results, errors, and side effects.
Cite the source or specification for each critical contract.
Map each contract to an executable test.
Record intentional differences, including security repairs.
Do not reproduce a known defect to match old output.

## Build the pilot

Keep verified upstream sources unchanged.
Apply reusable patches through the owning Ports recipe.
Use fresh outputs after compiler, sysroot, or configuration changes.
Build native generators for the host and libraries for the target.
Use host CPU, RAM, and disk limits for compilation.
Use guest resources to size target execution tests.
Complete the pilot before extending the migration to dependent components.
Remove obsolete patches after their regression passes without them.

## Verify behavior

Run baseline and candidate on the same inputs when both can execute.
Compare stdout, stderr, exit status, generated files, and relevant state changes.
Set `baseline` and `candidate` to captured runs of the same deterministic CLI case.

```sh
set -e
cmp "$baseline/stdout" "$candidate/stdout"
cmp "$baseline/stderr" "$candidate/stderr"
cmp "$baseline/status" "$candidate/status"
```

Declare numeric tolerances before comparison.
List every normalized field and its reason.
Keep meaningful differences visible.
Add fresh boundary, empty, malformed, and order-sensitive inputs.
Use independent expected results; candidate output alone is not an oracle.

If baseline execution is unavailable, use reviewed specifications or trusted captures with recorded provenance.
Report the missing live comparison.
Never install an obsolete toolchain to recreate it.
Keep target correctness and historical equivalence as separate claims.

Rerun relevant suites from fresh outputs.
Read executed, failed, skipped, and unresolved counts from runner results.
Zero executed tests establish no pass.
Check that a deliberate fault fails a regression in a disposable source copy.
Check that a changed output byte fails the comparator.
Restore the unmodified candidate before final verification.
Keep these checks in Ports, not in the skill package.

## Report evidence

Record commands, input hashes, target identity, loaded libraries, counts, and outstanding gaps.
Derive each scope's verified, partial, or unverified status from saved results.
Build success does not prove runtime behavior, equivalence, or hardware support.
Resume from recorded evidence only when source, configuration, tools, and inputs still match.

Method source: [Anthropic Code Modernization](https://github.com/anthropics/claude-plugins-official/blob/8f814f49002ff824e8a9ba43cf96112dc7f5948d/plugins/code-modernization/README.md).
