# Development OS sets

Build development OS sets with a build profile.
The profile accepts `base`, `comp`, and `etc` together for the aarch64 target with Clang.
Read the [build profile procedure](https://github.com/oxtech-ember/EmberBSD-SDK/blob/main/docs/build-profile.md).
Put the OS checkout, Binutils build, `work`, and `distfiles` in the client configuration.
Keep the OS, Ports, and SDK checkouts clean.
Run these commands from the SDK checkout:

```sh
"$sdk_python" scripts/packages.py --config /absolute/client.json profile-plan --profile /absolute/profile.json > plan.json
"$sdk_python" scripts/packages.py --config /absolute/client.json profile-build --profile /absolute/profile.json
```

`profile-build` runs the OS release builder and reuses stages with a matching input key.
Release finalization and target acceptance refuse these sets.
For a release kit, use the SDK [OS release procedure](https://github.com/oxtech-ember/EmberBSD-SDK/blob/main/docs/os-release.md).
For kernels, use `emberbsd-build-kernel`.
