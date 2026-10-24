---
name: emberbsd-repository-guide
description: Use when an EmberBSD task has no clear repository or skill owner.
---

# Select a developer skill

Read the [repository map](references/repositories.md).
Select one skill for the requested result.

| Task | Skill |
| --- | --- |
| Prepare a shared SDK workspace or sysroot | `emberbsd-prebuild-sdk` |
| Create or develop an application or example | `emberbsd-develop-app` |
| Cross-build a GCC16 kernel | `emberbsd-build-kernel` |
| Change a shared third-party recipe | `emberbsd-port-software` |
| Add or qualify a board | `emberbsd-add-board` |
| Build a static base set | `emberbsd-build-static-base` |
| Submit an authorized shared change | `emberbsd-contribute` |
| Change AI skills or client metadata | `emberbsd-maintain-skills` |

For retained personal third-party patches, select `emberbsd-personal-ports` from EmberBSD-User-Skills.
For device operation, select `emberbsd-user-guide` from that package.
Source editing alone does not require publication.
Separate reusable platform repairs from personal behavior changes.
Prepare those repairs at their public owner and submit them when authorized.

If the selected skill is absent, read the owning repository's public instructions.
Read its README and contribution rules before changes.
Use verified CLI or API calls.
Keep private material outside shared changes.
