# SDK workspace workflow

Read the [SDK README](https://github.com/oxtech-ember/EmberBSD-SDK).
Read the [layout contract](https://github.com/oxtech-ember/EmberBSD-SDK/blob/main/docs/prebuild-sdk.md).
If an SDK source checkout exists, use it.

The bundled `scripts/sdk.py` uses CPython 3.15 and its standard library.
It calls commands in the selected SDK checkout.
The SDK owns their checks.
From this skill directory, run these commands:

```sh
python3 scripts/sdk.py --sdk-source /absolute/EmberBSD-SDK inspect /absolute/prebuild-sdk
python3 scripts/sdk.py --sdk-source /absolute/EmberBSD-SDK sysroot --help
```

The launcher passes its interpreter and SDK source to the sysroot builder.
It also provides the `create` command.
The SDK command defines the build options.

From the SDK checkout, use these commands to inspect or create a workspace:

```sh
python3 scripts/inspect-prebuild-sdk.py /absolute/prebuild-sdk
python3 scripts/create-prebuild-sdk.py /absolute/prebuild-sdk
```

For an existing build tree, use `--adopt`:

```sh
python3 scripts/create-prebuild-sdk.py /absolute/prebuild-sdk --adopt /absolute/build
```

The `--adopt` option creates an alias to existing directories.
It does not copy or relocate build outputs.
Keep canonical paths until the build tools support relocation.
A correct layout does not prove ABI compatibility or compiler operation.

For sysroot builds, read the
[sysroot procedure](https://github.com/oxtech-ember/EmberBSD-SDK/blob/main/docs/sysroot.md).
Before you select inputs, read the script's help.
The SDK uses EmberBSD build rules and the verified Ports runtime.
It does not supply a different libc or compiler recipe.
Use GCC16 for target compilation.
Keep native host tools and target ELF files separate.
Record the source commits, tools, runtime receipts, configuration and output hashes.

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
The shared object cache is not a portable SDK release.
Publish only a verified SDK with its matching binary packages.
