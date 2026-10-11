# Contributing to Ember-Agent-Skills

This public repository packages developer skills for EmberBSD. Use English for
all source, documentation, comments, and commit messages.

- The installed skills instruct AI agents assisting developers and external
  contributors. Use concise task triggers, conditional actions and verified
  CLI/API commands; link owning tools instead of duplicating implementations.
  Keep that guidance in `SKILL.md` and bundled references; this file is for editing
  the plugin repository. Do not export private maintainer permissions, lab
  paths or personal assistant rules as requirements for users' applications.
- User operations and personal Ports customization belong to EmberBSD-User-Skills.
  Source editing alone does not make a personal change a shared contribution.
- Read `README.md` and `docs/packaging.md` before changing plugin packaging.
  Read `docs/codex.md` when changing the Codex adapter.
- Keep `plugin.json` as the canonical portable manifest. The marketplace entry
  identifies this plugin and points to the repository root with `./`.
- Put each skill in `skills/<name>/SKILL.md`. Resolve bundled references relative
  to that skill. Keep its YAML name aligned with the directory name.
- Read actual project sources before documenting an EmberBSD API or command.
  Repository ownership is not proof of an implemented or tested capability.
- Keep SDK contracts and build tools in their owning repositories. Skills invoke
  those tools and explain their results; they do not duplicate the implementation.
- Add MCP configuration only for an implemented, documented server. Do not ship
  placeholder endpoints, credentials, or private project data.
- New project utilities and checks must not use Python. Preserve upstream
  licenses and attribution when incorporating external material.
- Run `ruby scripts/check-package.rb`. With Codex available, also run it with
  `--codex` to check native marketplace discovery without changing user settings.
- Packaging checks do not prove skill quality. Review the manual scenarios in
  `docs/packaging.md` when changing the skill's behavior.
- Update the plugin version when publishing package changes. Keep changes scoped,
  preserve unrelated work, and use the existing working branch and remote unless
  the user or repository protection requires another workflow.
