# Keep guidance useful and current

Update guidance as part of the work that changes it: a verified port, confirmed
failure mode, changed build command, upstream acceptance, or retired workaround.
This is an event-driven maintenance rule; it does not claim that an unattended
monitor is running or authorize unrelated scheduled work.

Keep reusable decisions in this skill. Keep source-level recipes, executable
checks and detailed recovery instructions in the owning public repository.
Link them instead of maintaining a second implementation or copying full logs.
Never require a private wiki, local machine path, credential or personal image
to use a published skill.

Maintain the public user's workflow. Do not import a maintainer's direct-push
permissions, private lab setup or personal assistant rules into the installed
skill. When an external contributor improves these instructions, include the
guidance change in an Agent-Skills PR, cross-linking a separate code/port PR
when needed. Edit a source checkout, not only the installed plugin cache.

For each non-obvious workaround or compatibility case, preserve:

- the symptom and cause, distinguishing confirmed cause from a hypothesis;
- affected platform and version range, plus the source URL and checked revision;
- the smallest verified remedy and the command or regression that demonstrates it;
- known limits, upstream submission status and the condition that removes it.

Recheck unstable facts before using them. When upstream fixes the problem,
verify the new version, remove the local patch if appropriate, and replace the
old instruction. A removed workaround should not survive as a blanket ban.
Do not add rules based only on a single unexplained failure.

Before publishing a guidance update, inspect its links and run the package check
documented in the root README. Run native Codex discovery when available and
record the CLI version. For behavior changes, exercise a realistic relevant
scenario using only resources and side effects authorized for that check.
Discovery validates packaging; it does not demonstrate successful porting.

Update the package version, README use cases and installation/refresh guidance
when they change. Explain prerequisites, a copyable command, expected output,
and recovery or limits where relevant. Keep portable format checks separate
from client-specific installation and behavior evidence. Record each tested
client and version; do not infer package acceptance from a client support list.

## Client icon metadata

- `plugin.json`: set `extensions.com.openai.interface.composerIcon` and `logo`;
  resolve `./assets/emberbsd-logo.png` from the plugin root.
- `agents/openai.yaml`: set `interface.icon_small` and `icon_large`; resolve the
  same path from each skill root and bundle its PNG for standalone installation.
- ZCode/Claude's catalog `icon` does not populate Codex. Use the bundled PNG;
  the root SVG references an external image.
- Run `ruby scripts/check-package.rb --codex` in each package. It checks assets
  and native `plugin/read` paths using temporary profiles. Do not infer desktop
  rendering from CLI results; use client help for installed-package refresh.

