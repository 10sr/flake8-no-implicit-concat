"""Test NIC Chekcer."""

import ast
import unittest

from io import BytesIO
from tokenize import tokenize

from flake8_no_implicit_concat.checker import Checker


class TestChecker(unittest.TestCase):
    """Test NIC Chekcer."""

    def test_noerror(self):
        input = "a = 'aaa'"
        checker = Checker(
            ast.parse(input), tokenize(BytesIO(input.encode("utf-8")).readline)
        )
        actual = list(checker.run())
        expected = []
        self.assertEqual(actual, expected)
        return

    def test_error(self):
        # Detailed tests are done in run_flake8/Run.sh script
        input = "a = 'aaa' 'bbb'"
        checker = Checker(
            ast.parse(input), tokenize(BytesIO(input.encode("utf-8")).readline)
        )
        actual = list(checker.run())
        expected = [(1, 9, 'NIC001 Implicitly concatenated string literals', None)]
        self.assertEqual(actual, expected)
        return


if __name__ == "__main__":
    unittest.main()
