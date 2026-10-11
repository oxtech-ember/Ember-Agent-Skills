# Runtime and stream checks

Rebuild direct and transitive consumers after a compiler or library change.
Inspect target `DT_NEEDED` entries with `readelf`.
Inspect actually loaded libraries with target `ldd` or loader diagnostics.
Test exceptions and object exchange across shared-library boundaries.
Use one coherent C++ runtime per process.
Do not create fake SONAME links to hide an ABI mismatch.

Read [media provenance](https://github.com/neonix20b/EmberBSD-Ports/blob/aed5293/probes/media/PROVENANCE.md) for the recorded file-backend repairs.
That 2026-10-07 case used FFmpeg9.0.2 PIC and OpenCV5 FFmpeg9/POSIX filesystem fixes.
V4L was excluded.
Camera behavior remained untested.
Check the backend actually selected by the application.

For a GLib libintl mismatch, inspect ELF dependencies before metadata changes.
Base and pkgsrc libraries can expose different ABIs.
Use the narrow repair from the [owning recipe](https://github.com/neonix20b/EmberBSD-Ports/blob/aed5293/probes/media/build.sh).
Avoid blanket dependency corrections.

A complete frame sequence does not prove a complete container.
Compare trusted fixture length, decoder diagnostics, pixels, timestamps, and EOF.
State the fixture's limits.
Do not present a bounded regression as a general media validator.

For RNNoise0.2 ARM header failures, inspect the [accepted upstream repair](https://github.com/xiph/rnnoise/commit/372f7b4b76cde4ca1ec4605353dd17898a99de38).
Keep attribution and NEON support.
Check deterministic state and sample output.
That check does not measure perceived audio quality.
