import subprocess
import sys
import unittest
from pathlib import Path


class SolverTest(unittest.TestCase):
    def test_console_results(self) -> None:
        input_error = "Ошибка: введите три конечных числа."
        cases = (
            ("1 -3 2\n", 0, "Два корня: 1.0 и 2.0"),
            ("1\n2\n1\n", 0, "Двойной корень: -1.0"),
            ("1 0 1\n", 0, "Действительных корней нет."),
            ("0 2 -4\n", 0, "Корень: 2.0"),
            ("0 0 0\n", 0, "Уравнение выполняется при любом x."),
            ("0 0 5\n", 0, "Решений нет."),
            ("2 -1.5 0.25\n", 0, "Два корня: 0.25 и 0.5"),
            ("1 foo 2\n", 1, input_error),
            ("1 2\n", 1, input_error),
            ("1 2 3 4\n", 1, input_error),
            ("nan 0 1\n", 1, input_error),
            ("1e308 0 1\n", 1, "Ошибка: не удалось вычислить дискриминант."),
        )
        script = Path(__file__).with_name("quadsol.py")
        for coefficients, status, expected in cases:
            with self.subTest(coefficients=coefficients):
                result = subprocess.run(
                    [sys.executable, script],
                    input=coefficients,
                    capture_output=True,
                    encoding="utf-8",
                    timeout=5,
                    check=False,
                )
                self.assertEqual(result.returncode, status, result.stderr)
                if status:
                    self.assertEqual(result.stderr.strip(), expected)
                else:
                    self.assertTrue(result.stdout.rstrip().endswith(expected), result.stdout)
