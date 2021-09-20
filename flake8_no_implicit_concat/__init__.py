"""
Flake8 plugin that forbids implicit string literal concatenations.

Forbid implicitly concatenated string literals in all cases.
"""

from __future__ import generator_stop

import ast
import tokenize

from dataclasses import dataclass
from dataclasses import field
from typing import Iterable
from typing import Tuple

import more_itertools

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
    return (
        (a.end[0], a.end[1], "NIC001 Implicitly concatenated string literals", None)
        for (a, b) in more_itertools.pairwise(tokens_wo_ws)
        if a.type == b.type == tokenize.STRING
    )


@dataclass(frozen=True)
class Checker:
    """NIC Checker definition."""

    name = "no_implicit_concat"
    version = __version__
    # Avoid using variable type annotations for Python3.5 support
    tree: ast.AST
    file_tokens: Iterable[tokenize.TokenInfo]

    def run(self) -> Iterable[_ERROR]:
        """Run checker.

        :yields: Errors found.
        """
        yield from _check(self.file_tokens)
