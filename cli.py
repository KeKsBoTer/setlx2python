from antlr4 import FileStream, CommonTokenStream
from antlr4.error.ErrorListener import ErrorListener

from grammar.antlr.SetlXgrammarParser import SetlXgrammarParser
from grammar.antlr.SetlXgrammarLexer import SetlXgrammarLexer
from grammar.antlr.SetlXgrammarListener import SetlXgrammarListener

from transpiler import Transpiler
import ast
import sys


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
    """
    # TODO throw
    throw = ast.ImportFrom(module='setlx', names=[
        ast.alias(name='throw', asname=None)], level=0)
    """
    code = ast.Module(body=body)
    return code

def main():
    print(transpile(sys.argv[1]))

if __name__ == "__main__":
    main()