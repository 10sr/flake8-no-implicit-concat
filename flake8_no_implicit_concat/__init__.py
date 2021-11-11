"""Flake8 plugin that forbids implicit str/bytes literal concatenations."""

import ast
import sys
import tokenize

from typing import Iterable
from typing import Tuple

if sys.version_info < (3, 10):  # pragma: no cover
    from more_itertools import pairwise
else:
    from itertools import pairwise

from ._version import __version__

_ERROR = Tuple[int, int, str, None]


_ERROR_CODES = {  # [on_one_line][is_bytes]
    True: {
        True: "NIC101 Implicitly concatenated bytes literals on one line",
        False: "NIC001 Implicitly concatenated str literals on one line",
    },
    False: {
        True: "NIC102 Implicitly concatenated bytes literals over multiple lines",
        False: "NIC002 Implicitly concatenated str literals over multiple lines",
    },
}


def _check(tokens: Iterable[tokenize.TokenInfo]) -> Iterable[_ERROR]:
    tokens_wo_ws = (
        e
        for e in tokens
        if e.type
        not in (
            tokenize.NL,
            tokenize.NEWLINE,
            tokenize.INDENT,
            tokenize.DEDENT,
            tokenize.COMMENT,
        )
    )
    for (a, b) in pairwise(tokens_wo_ws):
        if not (a.type == b.type == tokenize.STRING):
            continue

        on_one_line = a.end[0] == b.start[0]

        literal_prefix = a.string.partition("'")[0].partition('"')[0]
        is_bytes = "b" in literal_prefix

        error_code = _ERROR_CODES[on_one_line][is_bytes]

        yield (a.end[0], a.end[1], error_code, None)


class Checker:
    """NIC Checker definition."""

    name = "no_implicit_concat"
    version = __version__

    def __init__(self, tree: ast.AST, file_tokens: Iterable[tokenize.TokenInfo]):
        """Intialize Checker.

        :param tree: File AST
        :param file_tokens: File tokens
        """
        self.tree = tree
        self.file_tokens = file_tokens
        return

    def run(self) -> Iterable[_ERROR]:
        """Run checker.

        :yields: Errors found.
        """
        yield from _check(self.file_tokens)
