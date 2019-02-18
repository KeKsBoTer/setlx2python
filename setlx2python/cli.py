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
from astor import to_source, string_repr

from antlr4 import FileStream, CommonTokenStream
from antlr4.error.ErrorListener import ErrorListener

from setlx2python.grammar.SetlXgrammarParser import SetlXgrammarParser
from setlx2python.grammar.SetlXgrammarLexer import SetlXgrammarLexer
from setlx2python.grammar.SetlXgrammarListener import SetlXgrammarListener

from setlx2python.transpiler import Transpiler, NotSupported
from . import __version__ as VERSION


class ParserErrorListener(ErrorListener):

    def __init__(self):
        ErrorListener.__init__(self)

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        raise SyntaxError("line " + str(line) + ":" + str(column) + " " + msg)


def transpile(file):
    input = FileStream(file, encoding="utf-8")
    lexer = SetlXgrammarLexer(input)
    stream = CommonTokenStream(lexer)
    parser = SetlXgrammarParser(stream)
    parser._listeners = [ParserErrorListener()]
    tree = parser.block()
    t = Transpiler(tree.blk)
    try:
        body = t.transpile()
    except NotSupported as e:
        print(e)
        sys.exit(2)
    code = ast.Module(body=body)
    return code


def pretty_source(source):
    """ Prettify the source.
    """
    # TODO we should split somewhere
    return ''.join((source))


def main():
    options = docopt(__doc__, version=VERSION)
    ast_tree = transpile(options["<file>"])
    print(to_source(ast_tree, pretty_source=pretty_source))
