from __future__ import generator_stop

"""
Flake8 plugin to reject any string literal concatenation.
Forbid implicitly concatenated string literals in all cases.
"""

import ast
import tokenize
from typing import Iterable, List, Tuple
from pprint import pprint

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
        (*a.end, "NIC001 Implicitly concatenated string literals", None)
        for (a, b) in more_itertools.pairwise(tokens_wo_ws)
        if a.type == b.type == tokenize.STRING
    )


@attr.s(frozen=True, auto_attribs=True)
class Checker:
    name = "no_implicit_concat"
    version = __version__
    tree: ast.AST
    file_tokens: List[tokenize.TokenInfo]

    def run(self) -> Iterable[_ERROR]:
        yield from _check(self.file_tokens)
