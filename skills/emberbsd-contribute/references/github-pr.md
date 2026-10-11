# GitHub PR commands

Set values from inspected repository metadata.
Use `target` as `owner/name` and `source_owner` as the head repository owner.
CLI `head` is a branch for same-repository PRs or `fork-owner:branch` for forks.
Set `body_file` to an absolute path.
Write the exact description into that file first.

```sh
git -C "$repo" status --short
git -C "$repo" diff --check
gh api -X GET "repos/$target/pulls" -f state=open -f head="$source_owner:$branch" -f base="$base" \
    --jq '.[] | {number, html_url}'
git -C "$repo" push -u "$push_remote" "$branch"
```

Set `number` from a unique matching PR.
Leave it empty when no PR exists.
Inspect ambiguous matches before changes.

```sh
if [ -n "$number" ]; then
    gh api --method PATCH "repos/$target/pulls/$number" \
        -f title="$title" -F body=@"$body_file"
else
    (cd "$repo" && gh pr create --repo "$target" --base "$base" --head "$head" \
        --title "$title" --body-file "$body_file")
fi
```

Explicit base and head arguments prevent interactive branch selection.
The REST update also works with older gh clients.
Preserve actual newlines in multiline descriptions.
Confirm the returned URL, target, base, head, and draft state.
Do not create a duplicate PR when a matching PR already exists.
