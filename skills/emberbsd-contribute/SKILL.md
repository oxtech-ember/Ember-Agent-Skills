---
name: emberbsd-contribute
description: Use when submitting an authorized shared EmberBSD fix, port, example, or documentation change.
---

# Submit a shared change

Read the target's contribution rules, license, and current AI policy.
Read [submission checks](references/submission-checks.md).
Read [design principles](references/design-principles.md) before you change shared code.
For GitHub, read [PR commands](references/github-pr.md).

1. Identify the owner, accepted base, and actual submission channel.
   Send shared dependency recipes and patches to Ports.
2. Reproduce the problem and prepare a focused fix.
3. Run the required checks on the proposed revision.
4. Inspect the complete diff and preserve source attribution.
5. Push an authorized topic branch or fork branch.
6. Create or update the matching contribution.
7. Report its returned URL and actual state.

A logic or behavior fix needs a causal regression test.
A trivial fix needs no regression test: step order, typos, paths, and similar mechanical corrections.
Such tests cost time and add no value.

EmberBSD welcomes external contributors through pull requests.
Personal behavior changes do not require publication.
Separate reusable platform repairs from those changes.
If publication is authorized, complete submission instead of leaving the tested repair only in a local checkout.
If permission is missing, prepare a reviewable patch and its checks before asking.
Respect a refusal and report the patch as unsubmitted.
Do not request authorization already granted.
Keep private material outside the submission.
Do not assume upstream write or merge permission.
Do not overwrite another contributor's branch.
Merge only when authorized.
Use a permitted draft for missing required validation.
Keep failed tests visible.
