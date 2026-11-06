# Install SDK components

Read the SDK's [first installation](https://github.com/oxtech-ember/EmberBSD-SDK/blob/main/docs/bootstrap-client.md)
and [component client](https://github.com/oxtech-ember/EmberBSD-SDK/blob/main/docs/sdk-client.md) procedures.
Use the public HTTPS catalog at [emberbsd-pkg.oxteam.me](https://emberbsd-pkg.oxteam.me/current.p7m).
The publisher uses S3; consumers need no storage credentials or AWS CLI.

Inspect an existing SDK before installing another prefix.
On a supported host, use the minimal bootstrap without requiring an existing Python, compiler, or Ports checkout.
Select only components required by the user's task.
Use the client's catalog and plan to check availability, host, target/ABI, dependencies, and download size.
Do not assume that every compiler, sysroot, or host platform is already published.
Follow the owner's current support boundaries.
The first-install shell bootstrap currently selects Darwin arm64 only.
On Linux, check for a compatible installed prefix and published components.
If no host bootstrap exists, follow the SDK [Linux bootstrap](https://github.com/oxtech-ember/EmberBSD-SDK/blob/main/docs/linux-bootstrap.md).
Acquire the initial native tools through Ports, then return to the client.
The client's configured source path uses a prepared native prefix; it does not bootstrap its first compiler.

Reuse compatible installed components first.
Then install matching signed binaries through the client.
Build missing packages through the client's configured Ports source path.
Use the [workspace workflow](workflow.md) when source preparation or a sysroot build is necessary.
Do not treat signature errors, corrupted archives, or network failures as missing binaries.
Keep signature and integrity checks enabled.

Share the native prefix and package cache across tasks.
Keep one sysroot per target/ABI.
Do not download another host toolchain for each target.
Use the client's supported operations for cache cleanup and component changes.
Do not describe installation as an accepted compiler, application, or device check.
