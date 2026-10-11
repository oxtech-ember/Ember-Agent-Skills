# Prepare the compiler

Read the [Ports cross-build procedure](https://github.com/oxtech-ember/EmberBSD-Ports/blob/main/profiles/development-toolchain/cross/README.md).
Use its original archive URL and SHA256.
Verify the selected Ports and pkgsrc revisions.
Investigate a hash mismatch before extraction.

Set `ports`, `pkgsrc`, `gcc_archive`, `tools`, and `work` to absolute paths.
Use paths without whitespace, as the recipe requires.
The `tools` directory must contain fork-built host tools and target binutils.
Use a new compiler work directory.
Set `jobs` from available CPU, RAM, and disk capacity.

```sh
set -e
command -v gcc g++
gcc -dumpfullversion
gcc -dumpmachine
g++ -dumpfullversion
g++ -dumpmachine
git -C "$ports" submodule status
git -C "$ports" submodule update --init --depth 1 upstream/pkgsrc
sh "$ports/scripts/prepare-pkgsrc.sh" "$pkgsrc" development-toolchain
HOST_CC=gcc HOST_CXX=g++ CROSS_JOBS="$jobs" \
    sh "$ports/profiles/development-toolchain/cross/build.sh" --kernel \
    "$pkgsrc" "$gcc_archive" "$tools" "$work"
"$work/toolchain/bin/aarch64--netbsd-gcc" -dumpfullversion
"$work/toolchain/bin/aarch64--netbsd-gcc" -dumpmachine
```

The export command requires a nonexistent destination.
Omit it only for a verified export from the selected revisions.
The recipe builds isolated host math libraries when no accepted prefix is supplied.
Its README defines optional host math reuse.
Keep source hashes, patches, math repairs, and executable regressions in Ports.
Do not copy a compiler workaround into skills.
The installed split-DWARF check verifies the driver's target tool lookup.
Keep compiler versions, triplets, library hashes, and real test results.
