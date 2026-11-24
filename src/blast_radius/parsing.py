import tree_sitter_python as tspython
from tree_sitter import Language, Parser, Tree

PY_LANGUAGE = Language(tspython.language())
parser = Parser(PY_LANGUAGE)


def parse(src_code: bytes) -> Tree:
    tree = parser.parse(src_code)
    return tree
