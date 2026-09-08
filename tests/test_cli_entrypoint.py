import subprocess
import sys
import unittest
from pathlib import Path


class TestEntrypoints(unittest.TestCase):
    def test_cli_can_run_directly(self):
        project_root = Path(__file__).resolve().parents[1]
        result = subprocess.run(
            [sys.executable, "src/cli.py"],
            input="7\n",
            text=True,
            capture_output=True,
            cwd=str(project_root),
        )

        self.assertEqual(result.returncode, 0)
        self.assertIn("GESTOR DE TAREAS - CLI", result.stdout)

    def test_package_init_can_run_directly(self):
        project_root = Path(__file__).resolve().parents[1]
        result = subprocess.run(
            [sys.executable, "src/__init__.py"],
            input="7\n",
            text=True,
            capture_output=True,
            cwd=str(project_root),
        )

        self.assertEqual(result.returncode, 0)
        self.assertIn("GESTOR DE TAREAS - CLI", result.stdout)
