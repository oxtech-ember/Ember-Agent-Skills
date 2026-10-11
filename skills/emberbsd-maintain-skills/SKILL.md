---
name: emberbsd-maintain-skills
description: Use when changing EmberBSD AI skill instructions, task boundaries, plugin packaging, or client icon metadata.
---

# Maintain AI skills

Read the source package's AGENTS.md and packaging documents.
Read [skill changes](references/skill-changes.md).
For icon faults, read [icon metadata](references/icon-metadata.md).

1. Identify one task and its discovery condition.
2. Keep its entry short.
3. Move conditional details into local references.
4. Use simple active instructions in ASD-STE100 style.
5. Keep fixes and executable regressions in their owning repository.
6. Update package versions and affected client metadata.
7. Run package checks and relevant behavior scenarios.
8. Record the tested client and remaining gaps.

Edit the source package, not only an installed cache.
Each skill must work without sibling directories.
Use `emberbsd-contribute` for an authorized shared submission.
Verified lessons can trigger updates; they do not create a monitoring schedule.
Package discovery does not prove assistant behavior or desktop rendering.
