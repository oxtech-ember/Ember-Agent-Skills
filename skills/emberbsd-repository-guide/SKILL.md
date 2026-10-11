---
name: emberbsd-repository-guide
description: "Use when developing EmberBSD applications, changing OS/SDK/Runtime, adding boards, upgrading shared dependencies, or contributing reusable fixes/ports. Device operation and personal customization use EmberBSD-User-Skills."
---

# EmberBSD repository guide

Use the owning repository's CLI/API. Load only needed references, relative to
this installed skill.

## Inspect and route

Set `repo` to the actual checkout. Preserve unrelated changes:

```sh
git -C "$repo" status --short
git -C "$repo" rev-parse HEAD
rg --files --hidden -g AGENTS.md -g '!.git/**' "$repo"
```

Read applicable AGENTS.md and subsystem README/CONTRIBUTING; inspect sanitized
remote identities before network operations. Use [ownership](references/repositories.md):
personal source changes stay in User-Skills; shared fixes belong here.

| Task | Load |
| --- | --- |
| User's application | [Application workflow](references/developing-applications.md) |
| Third-party software, compiler, ABI | [Ports and compiler selection](references/ports.md) |
| Board bring-up or validation | [Board workflow](references/adding-boards.md) |
| Static base/image | [Static builds](references/static-builds.md) |
| Authorized shared contribution | [Submission workflow](references/contributions.md) |
| Changed reusable guidance | [Maintenance](references/maintenance.md) |

## Execute and verify

Check each result before running dependent commands. For `rg`, status 1 means
no match; status 2 or higher means a search error.

1. Find actual commands/APIs/examples/tests with `rg`; report missing interfaces.
   SDK/Runtime ownership alone establishes no implemented API.
2. Call owning tools; keep shared implementations/regressions in OS/Ports/SDK/Runtime
   and application-specific code in the user's project.
3. Reproduce, fix the cause and run relevant checks. Distinguish source, build,
   host/VM and hardware evidence; preserve real exit statuses.
4. Follow task authorization for publication/flashing/reboot. Public examples
   need public inputs; keep private code, credentials and images private.
5. Complete authorized tested contributions through the accepting project's
   channel. Report revision, commands/results, gaps and submission URL/state;
   update changed reusable guidance.

EmberBSD contributions: English, retained licenses/authorship, local C conventions,
no new Python utilities/tests. Independent applications keep their conventions;
existing upstream dependencies follow their owning builds.
