"""
setlx2python
 
Usage:
  setlx2python <file>
  setlx2python -h | --help
  setlx2python --version
 
Options:
  -h --help                         Show this screen.
  --version                         Show version.
 
Examples:
  setlx2python hello.stlx
 
Help:
  For help using this tool, please open an issue on the Github repository:
  https://github.com/KeKsBoTer/setlx2python
"""

import ast
import sys
from docopt import docopt
from astor import to_source

from antlr4 import FileStream, CommonTokenStream
from antlr4.error.ErrorListener import ErrorListener

from .grammar.SetlXgrammarParser import SetlXgrammarParser
from .grammar.SetlXgrammarLexer import SetlXgrammarLexer
from .grammar.SetlXgrammarListener import SetlXgrammarListener

from .transpiler import Transpiler

from . import __version__ as VERSION


class ParserErrorListener(ErrorListener):

    def __init__(self):
        ErrorListener.__init__(self)

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        raise SyntaxError("line " + str(line) + ":" + str(column) + " " + msg)


def transpile(file):
    input = FileStream(file)
    lexer = SetlXgrammarLexer(input)
    stream = CommonTokenStream(lexer)
    parser = SetlXgrammarParser(stream)
    parser._listeners = [ParserErrorListener()]
    tree = parser.block()
    t = Transpiler(tree.blk)
    body = t.transpile()
    code = ast.Module(body=body)
    return code


def main():
    options = docopt(__doc__, version=VERSION)
    ast_tree = transpile(options["<file>"])
    print(to_source(ast_tree))
