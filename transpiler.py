
from antlr4 import FileStream, CommonTokenStream
from antlr4.error.ErrorListener import ErrorListener

from grammar.setlx.antlr.SetlXgrammarParser import SetlXgrammarParser
from grammar.setlx.antlr.SetlXgrammarLexer import SetlXgrammarLexer
from grammar.setlx.antlr.SetlXgrammarListener import SetlXgrammarListener

from grammar.setlx.state import SetlxState
import ast


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
    state = SetlxState()
    body = tree.blk.to_python(state)
    # TODO throw
    throw = ast.ImportFrom(module='setlx', names=[
        ast.alias(name='throw', asname=None)], level=0)
    imports = [throw] + state.imports.to_python(state)
    body = imports + body
    code = ast.Module(body=body)
    return code
