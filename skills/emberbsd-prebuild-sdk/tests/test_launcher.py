# SPDX-License-Identifier: MIT
# Origin: EmberBSD contributors (AI-assisted).
"""Launcher transport checks; SDK build behavior belongs to the SDK tests."""

import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest

LAUNCHER = Path(__file__).resolve().parents[1] / 'scripts' / 'sdk.py'


class LauncherTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory(prefix='ember-sdk-skill-')
        self.root = Path(self.temporary.name).resolve()
        self.sdk = self.root / 'SDK source Ω'
        (self.sdk / 'scripts').mkdir(parents=True)
        self.fixture = (
            'import json, os, sys\n'
            'print(json.dumps({"script": os.path.basename(__file__), '
            '"args": sys.argv[1:], "cwd": os.getcwd(), '
            '"isolated": sys.flags.isolated, "no_site": sys.flags.no_site, '
            '"no_bytecode": sys.dont_write_bytecode}))\n'
        )
        for name in ('create-prebuild-sdk.py', 'inspect-prebuild-sdk.py', 'build-sysroot.py'):
            (self.sdk / 'scripts' / name).write_text(self.fixture, encoding='utf-8')

    def tearDown(self):
        self.temporary.cleanup()

    def run_launcher(self, *args, launcher=LAUNCHER):
        return subprocess.run([sys.executable, '-B', '-I', '-S', str(launcher), '--sdk-source', str(self.sdk), *args], cwd=self.root, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=False)

    def test_create_preserves_literal_arguments(self):
        values = ['workspace with spaces', '$(touch accidental-file)', '--adopt', 'Ω build']
        result = self.run_launcher('create', '--', *values)
        self.assertEqual(result.returncode, 0, result.stderr)
        row = json.loads(result.stdout)
        self.assertEqual(row['script'], 'create-prebuild-sdk.py')
        self.assertEqual(row['args'], values)
        self.assertEqual(row['cwd'], str(self.root))
        self.assertEqual((row['isolated'], row['no_site'], row['no_bytecode']), (1, 1, True))
        self.assertFalse((self.root / 'accidental-file').exists())

    def test_sysroot_passes_selected_source_and_interpreter(self):
        result = self.run_launcher('sysroot', '--plan', '--sdk', '/workspace')
        self.assertEqual(result.returncode, 0, result.stderr)
        arguments = json.loads(result.stdout)['args']
        self.assertEqual(arguments[:3], ['--sdk-source', str(self.sdk), '--python'])
        self.assertTrue(Path(arguments[3]).samefile(sys.executable))
        self.assertEqual(arguments[4:], ['--plan', '--sdk', '/workspace'])

    def test_sysroot_rejects_conflicting_selection(self):
        for option in ('--sdk-source=/other', '--python', '--python=/other'):
            with self.subTest(option=option):
                result = self.run_launcher('sysroot', option)
                self.assertEqual(result.returncode, 2)
                self.assertIn(b'do not repeat', result.stderr)

    def test_missing_command_fails(self):
        (self.sdk / 'scripts' / 'inspect-prebuild-sdk.py').unlink()
        result = self.run_launcher('inspect', '/workspace')
        self.assertEqual(result.returncode, 2)

    def test_command_link_cannot_escape_selected_sdk(self):
        script = self.sdk / 'scripts' / 'inspect-prebuild-sdk.py'
        script.unlink()
        outside = self.root / 'outside.py'
        outside.write_text('raise RuntimeError("must not execute")\n', encoding='utf-8')
        script.symlink_to(outside)
        result = self.run_launcher('inspect', '/workspace')
        self.assertEqual(result.returncode, 2)
        self.assertNotIn(b'must not execute', result.stderr)

    def test_propagates_child_failure(self):
        (self.sdk / 'scripts' / 'inspect-prebuild-sdk.py').write_text('raise SystemExit(7)\n', encoding='utf-8')
        self.assertEqual(self.run_launcher('inspect', '/workspace').returncode, 7)

    def test_standalone_copied_skill(self):
        copied = self.root / 'installed skill' / 'scripts' / 'sdk.py'
        copied.parent.mkdir(parents=True)
        shutil.copyfile(LAUNCHER, copied)
        result = self.run_launcher('inspect', '/workspace', launcher=copied)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(json.loads(result.stdout)['script'], 'inspect-prebuild-sdk.py')


if __name__ == '__main__':
    unittest.main()
