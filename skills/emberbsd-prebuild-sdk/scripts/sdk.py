#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
# Origin: EmberBSD contributors (AI-assisted).
"""Run canonical SDK commands from an explicitly selected source checkout."""

import argparse
import os
from pathlib import Path
import stat
import sys

sys.dont_write_bytecode = True

COMMANDS = {
    'create': 'create-prebuild-sdk.py',
    'inspect': 'inspect-prebuild-sdk.py',
    'sysroot': 'build-sysroot.py',
}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--sdk-source', required=True, type=Path)
    parser.add_argument('operation', choices=COMMANDS)
    parser.add_argument('arguments', nargs=argparse.REMAINDER)
    options = parser.parse_args()
    try:
        if sys.implementation.name != 'cpython' or sys.version_info[:2] != (3, 15):
            raise ValueError('the current SDK host profile requires CPython 3.15')
        source = options.sdk_source.resolve(strict=True)
        if not source.is_dir():
            raise ValueError('SDK source must be a directory')
        script = (source / 'scripts' / COMMANDS[options.operation]).resolve(strict=True)
        script.relative_to(source)
        if not stat.S_ISREG(script.stat().st_mode):
            raise ValueError('SDK command must be a regular file')
        arguments = options.arguments
        if arguments[:1] == ['--']:
            arguments = arguments[1:]
        if options.operation == 'sysroot':
            if any(arg.split('=', 1)[0] in ('--sdk-source', '--python') for arg in arguments):
                raise ValueError('the launcher selects --sdk-source and --python; do not repeat them')
            arguments = ['--sdk-source', str(source), '--python', sys.executable, *arguments]
        # Replace this process so the SDK CLI retains normal signal ownership.
        os.execv(sys.executable, [sys.executable, '-B', '-I', '-S', str(script), *arguments])
    except (OSError, ValueError) as error:
        parser.exit(2, f'sdk.py: {error}\n')


if __name__ == '__main__':
    main()
