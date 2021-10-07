"""Flake8 plugin that forbids implicit str/bytes literal concatenations."""

from __future__ import generator_stop

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
        if a.end[0] == b.start[0]:
            yield (
                a.end[0],
                a.end[1],
                "NIC001 Implicitly concatenated string literals in one line",
                None,
            )
        else:
            yield (
                a.end[0],
                a.end[1],
                "NIC002 Implicitly concatenated string literals over multiple lines",
                None,
            )
    return


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
        return
