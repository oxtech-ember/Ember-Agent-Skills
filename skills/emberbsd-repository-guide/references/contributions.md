# Tested contributions

Apply this to an authorized shared fix/port/example/documentation contribution.
Personal application or Ports work does not require publication. If publication
is outside task scope, complete a reviewable patch before requesting permission.

## Inspect, test, submit

1. Identify owner, accepted base, existing issue/PR and current
   AGENTS/CONTRIBUTING, tests, license and AI policy. A GitHub mirror may accept
   only mailing-list patches or problem reports.
2. Reproduce and fix the cause; retain a failing-before/passing-after regression.
   A port needs real build/install/runtime evidence; package claims additionally
   need install/remove/reinstall. Documentation needs instruction/link checks.
3. Inspect remotes and changes. Use a topic branch; use a fork without upstream
   branch access. Preserve unrelated work, authorship and private material.
4. Run relevant checks on the proposed revision; real failures remain failures.
   State unavailable validation and use a draft only when the target permits it.
5. Push the verified topic branch and open/update the focused contribution.
   Respect branch protection; do not overwrite others or auto-merge.

For a GitHub PR target, set `repo`, `target` (`owner/name`), `base`, `branch`,
`push_remote`, `source_owner`, `head` and `title` from inspected metadata.
`source_owner` is the head repository's owner; CLI `head` is the branch for a
same-repository PR or fork-owner:branch for a fork. Use an absolute `body_file`:

```sh
git -C "$repo" status --short
git -C "$repo" diff --check
gh api -X GET "repos/$target/pulls" -f state=open -f head="$source_owner:$branch" -f base="$base" \
    --jq '.[] | {number, html_url}'
git -C "$repo" push -u "$push_remote" "$branch"
```

Set `number` from a unique matching PR, or empty if none; inspect ambiguous results.
Update the match or create the missing PR:

```sh
if [ -n "$number" ]; then
    gh api --method PATCH "repos/$target/pulls/$number" \
        -f title="$title" -F body=@"$body_file"
else
    (cd "$repo" && gh pr create --repo "$target" --base "$base" --head "$head" \
        --title "$title" --body-file "$body_file")
fi
```

Write the exact description to `body_file` first;
use the repository template.
Lead with trigger and resulting behavior, then tested revision/platform/tools,
commands/results, limits and provenance. Record returned URL and actual state:
prepared, submitted, reviewed, merged or released. Address reviews in that PR.

## Upstream and evidence

An EmberBSD change includes project integration. A reusable upstream change is
a minimal patch against upstream's current accepted base; test it separately and
cross-link submissions. Send through its real channel only when authorized.
A reproduced unfixed bug belongs in an authorized issue/report, not an empty PR.

Read current [pkgsrc submission rules](https://www.netbsd.org/docs/pkgsrc/submit.html)
for pkgsrc-wip/pkglint/problem reports and
[NetBSD AI/commit policy](https://www.netbsd.org/developers/commit-guidelines.html)
before submission. Prior written core approval for committing LLM-generated code
was required when checked 2026-10-06; recheck the policy and disclose assistance.
Tests do not replace an accepting project's approval.
