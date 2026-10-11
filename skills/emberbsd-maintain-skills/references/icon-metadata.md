# Icon metadata

ZCode and Claude Code use the catalog's `icon` URL.
That field does not supply Codex icons.
Inspect Codex metadata when only those clients display the logo.

| Metadata | Path base |
| --- | --- |
| `plugin.json`: `extensions.com.openai.interface.composerIcon` and `logo` | Plugin root |
| `agents/openai.yaml`: `interface.icon_small` and `icon_large` | Each skill root |

Use `./assets/emberbsd-logo.png` at both bases.
Bundle a PNG copy with every skill for standalone installation.
The root SVG contains an external image reference.
Use the bundled PNG directly.

Run `check-package.rb --codex` from the source package.
It checks native plugin and skill paths through temporary profiles.
It does not change saved settings.
Discovery alone does not expose the icon fields.
Inspect installed versions through the client's CLI before refreshing a cached package.
Check desktop rendering separately when a desktop client is available.
