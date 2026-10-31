# Change a skill

Use one task per skill.
Write a narrow description that states when the skill applies.
Keep descriptions within 25 words and entry prose within 250 words.
Keep each reference within 500 prose words.
Keep procedural sentences within 20 words.
Use active voice and one instruction per sentence.
Use one term for each technical concept.
Preserve literal CLI, API, path, and configuration strings.
These limits support ASD-STE100 style; they do not certify dictionary compliance.

Keep all linked instructions, icons, and metadata inside the skill directory.
Refer to another skill by name instead of linking to its files.
Provide an owning public procedure when the other skill can be absent.
Do not require private wiki pages, lab paths, or credentials.
Link build reuse rules to the common [input key rule](https://github.com/oxtech-ember/EmberBSD-SDK/blob/main/docs/input-keys.md).
Do not write rules that reread or rehash inputs that a git hash or input key already identifies.
Route hardware, SoC, bootloader, layout, and current support guidance to DevBoards.
Keep OS mechanism documentation beside its subsystem.
Route common build orchestration, sysroots, and release kits to SDK.
Route dependency recipes and upstream patches to Ports.
Route standalone UI applications to Examples or their own repository.
Keep skills concise; link to owner contracts instead of copying them.
Do not use OS documentation as an umbrella for other projects.

For a compatibility lesson, record symptom, cause, affected versions, source, and checked revision.
Add the verified remedy, check, limits, upstream state, and removal condition.
Retest changing facts.
Remove obsolete guidance after the regression passes without the workaround.

Set `skills_repo` to the source package checkout.

```sh
(cd "$skills_repo" && ruby scripts/check-package.rb)
if command -v codex >/dev/null 2>&1; then
    (cd "$skills_repo" && ruby scripts/check-package.rb --codex)
    codex --version
fi
```

Keep manifests, catalog versions, README scope, and adapter documents consistent.
Exercise direct task selection and standalone installation.
Record actual application behavior separately from package discovery.
