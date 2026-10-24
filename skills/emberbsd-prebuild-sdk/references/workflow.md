# SDK workspace workflow

Read the [SDK README](https://github.com/oxtech-ember/EmberBSD-SDK).
Read the [layout contract](https://github.com/oxtech-ember/EmberBSD-SDK/blob/main/docs/prebuild-sdk.md).
Read the [SDK tool selection policy](https://github.com/oxtech-ember/EmberBSD-SDK/blob/main/docs/tool-selection.md), including current enforcement gaps.
If an SDK source checkout exists, use it.

The bundled `scripts/sdk.py` uses CPython 3.15 and its standard library.
Set `sdk_python` to its verified absolute SDK interpreter path.
It calls commands in the selected SDK checkout.
The SDK owns their checks.
From this skill directory, run these commands:

```sh
"$sdk_python" scripts/sdk.py --sdk-source /absolute/EmberBSD-SDK inspect /absolute/prebuild-sdk-aarch64
"$sdk_python" scripts/sdk.py --sdk-source /absolute/EmberBSD-SDK sysroot --help
```

The launcher passes its interpreter and SDK source to the builder.

From the SDK checkout, use these commands to inspect or create a workspace:

```sh
"$sdk_python" scripts/create-prebuild-sdk.py /absolute/prebuild-sdk-aarch64 --target aarch64
"$sdk_python" scripts/inspect-prebuild-sdk.py /absolute/prebuild-sdk-aarch64
"$sdk_python" scripts/create-prebuild-sdk.py /absolute/prebuild-sdk-amd64 --target amd64
```

For an existing target workspace, use `--adopt`:

```sh
"$sdk_python" scripts/create-prebuild-sdk.py /absolute/prebuild-sdk-aarch64 --target aarch64 --adopt /absolute/aarch64-build
```

`--adopt` creates an alias without relocating outputs.
Keep canonical paths until relocation is supported.
The manifest declares the target; the alias and host architecture do not.
Inspect unknown legacy targets without rewriting their context.
Read the SDK migration boundary before changes.
The builder requires a matching declared target.

For sysroot builds, read the
[sysroot procedure](https://github.com/oxtech-ember/EmberBSD-SDK/blob/main/docs/sysroot.md).
Before you select inputs, read the script's help.
The SDK uses EmberBSD build rules and the verified Ports runtime.
It does not supply a different libc or compiler recipe.
Reuse current dependencies from the [common Ports recipes](https://github.com/oxtech-ember/EmberBSD-Ports/tree/main/pkgsrc).
Check direct, transitive, build, and test dependencies, including host tools.
Use the [Ports update contract](https://github.com/oxtech-ember/EmberBSD-Ports/blob/main/docs/update-ports.md) for the shared graph and patch set.
Move dependency repairs out of the sysroot or cache into Ports with their regressions.
Use `emberbsd-contribute` or the [public contribution procedure](https://github.com/oxtech-ember/EmberBSD/blob/main/CONTRIBUTING.md) for authorized submissions.
Prepare the shared patch before requesting any missing publication permission.
Use SDK cross GCC16 for targets and SDK native GCC16 for host programs.
Require SDK provenance for all build tools, including interpreters and generators.
Reject ambient PATH, system compilers, and host package-manager substitutes.
Check resolved paths, hashes, driver-selected tools, cached configuration, and nested commands before compilation.
HOST_CC/HOST_CXX do not suffice when the SDK overrides them.
Missing selectors or tools require a shared SDK/Ports repair with refusal tests.
Do not hide that gap with a local wrapper or PATH change.
Keep host ABI inputs separate from target files.
Record the source commits, tools, runtime receipts, configuration and output hashes.

Use shared objects and packages for each target ABI.
Do not create separate build roots for tasks or boards.
Keep incompatible ABIs separate.
Each developer maintains one current sysroot per target ABI.
Build a stale sysroot's replacement alongside it.
Replace the old sysroot after acceptance.
Before object reuse, compare the recorded inputs with the current inputs.
For compatible source changes, use the incremental build rules.
Use separate install stages for runtime and developer packages.
Check which package owns each file.
A failed build does not validate an older output at the same path.

Read [host platforms](https://github.com/oxtech-ember/EmberBSD-SDK/blob/main/docs/host-platforms.md)
for Windows and POSIX build environments.
Portable path checks do not prove native Windows build support.
Record the actual tests for each platform separately.

Read the [distribution boundary](https://github.com/oxtech-ember/EmberBSD-SDK/blob/main/docs/distribution.md)
before preparing a binary SDK.
Publish only a verified SDK with matching binary packages.
