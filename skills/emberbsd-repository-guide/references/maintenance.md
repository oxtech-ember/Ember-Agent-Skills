# Maintain AI guidance

Update the source package when verified work changes a reusable decision. Write
compact task triggers, conditional actions and CLI/API calls. Load detailed
references only when needed. Keep executable fixes, regressions and recovery
procedures in their owning public repository; link rather than duplicate them.
Do not require private paths/wiki/credentials or edit only an installed cache.

For a compatibility lesson retain symptom/cause, affected versions, source URL
and checked revision, verified remedy/check, remaining limits, upstream state
and removal condition. Recheck changing facts; remove obsolete patches after
the regression passes without them. No scheduled monitoring is implied.

Before publishing, check links/commands and relevant application scenarios.
Set `skills_repo` to the source package checkout; Codex checks are conditional:

```sh
(cd "$skills_repo" && ruby scripts/check-package.rb)
if command -v codex >/dev/null 2>&1; then
    (cd "$skills_repo" && ruby scripts/check-package.rb --codex)
    codex --version
fi
```

Update unreleased package metadata consistently, README scope and affected
adapter docs. Record tested clients separately; discovery proves packaging,
not assistant behavior, successful porting or desktop rendering. Contributions
use [the submission workflow](contributions.md) and task authorization.

## Icon metadata

- `plugin.json`: `extensions.com.openai.interface.composerIcon` and `logo`
  resolve `./assets/emberbsd-logo.png` from the plugin root.
- `agents/openai.yaml`: `interface.icon_small` and `icon_large` resolve that path
  from each skill root; bundle the PNG for standalone installation.
- ZCode/Claude catalog `icon` does not populate Codex. The root SVG references an
  external image. `check-package.rb --codex` checks bundled PNG/native paths in
  temporary profiles; use client CLI help for installed-package refresh.
