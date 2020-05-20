"""NIC Checker definition."""

from __future__ import generator_stop

import ast
import tokenize

from typing import Iterable, Tuple

import attr
import more_itertools

from . import __version__

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
    return (
        (a.end[0], a.end[1], "NIC001 Implicitly concatenated string literals", None)
        for (a, b) in more_itertools.pairwise(tokens_wo_ws)
        if a.type == b.type == tokenize.STRING
    )


@attr.s(frozen=True)
class Checker:
    """NIC Checker definition."""

    name = "no_implicit_concat"
    version = __version__
    # Avoid using variable type annotations for Python3.5 support
    tree = attr.ib(type=ast.AST)  # type: ast.AST
    file_tokens = attr.ib(
        type=Iterable[tokenize.TokenInfo]
    )  # type: Iterable[tokenize.TokenInfo]

    def run(self) -> Iterable[_ERROR]:
        """
        Run checker.

        :yields: Errors found.
        """
        yield from _check(self.file_tokens)
