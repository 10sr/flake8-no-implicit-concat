"""Test NIC Chekcer."""

import ast
import tokenize
import unittest

from io import BytesIO
from typing import Iterable, Tuple

from flake8_no_implicit_concat.checker import Checker


def _tokenize(input: str) -> Iterable[tokenize.TokenInfo]:
    return tokenize.tokenize(BytesIO(input.encode("utf-8")).readline)


class TestChecker(unittest.TestCase):
    """Test NIC Chekcer."""

    def test_noerror(self) -> None:
        """Test checker with valid input."""
        input = "a = 'aaa'"
        checker = Checker(ast.parse(input), _tokenize(input))
        actual = list(checker.run())
        expected = []  # type: Iterable[Tuple[int, int, str, None]]
        self.assertEqual(actual, expected)
        return

    def test_error(self) -> None:
        """Test checker with invalid input."""
        # Detailed tests are done in run_flake8/Run.sh script
        input = "a = 'aaa' 'bbb'"
        checker = Checker(ast.parse(input), _tokenize(input))
        actual = list(checker.run())
        expected = [(1, 9, "NIC001 Implicitly concatenated string literals", None)]
        self.assertEqual(actual, expected)
        return


if __name__ == "__main__":
    unittest.main()
