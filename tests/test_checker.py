"""Test NIC Chekcer."""

import ast
import tokenize
import unittest

from io import BytesIO
from typing import Iterable

from flake8_no_implicit_concat import Checker


def _tokenize(input_: str) -> Iterable[tokenize.TokenInfo]:
    return tokenize.tokenize(BytesIO(input_.encode("utf-8")).readline)


class TestChecker(unittest.TestCase):
    """Test NIC Chekcer."""

    def test_noerror(self) -> None:
        """Test checker with valid input."""
        input_ = "a = 'aaa'"
        checker = Checker(ast.parse(input_), _tokenize(input_))
        result = checker.run()
        self.assertEqual(len(list(result)), 0)
        return

    def test_error(self) -> None:
        """Test checker with invalid input."""
        # Contents of results are checked in run_flake8/
        input_ = "a = 'aaa' 'bbb'"
        checker = Checker(ast.parse(input_), _tokenize(input_))
        result = checker.run()
        self.assertEqual(len(list(result)), 1)
        return


if __name__ == "__main__":
    unittest.main()
