
from antlr4 import FileStream, CommonTokenStream
from grammar.setlx.antlr.SetlXgrammarParser import SetlXgrammarParser
from grammar.setlx.antlr.SetlXgrammarLexer import SetlXgrammarLexer
from grammar.setlx.antlr.SetlXgrammarListener import SetlXgrammarListener

from grammar.setlx.state import SetlxState
import ast


def transpile(file):
    input = FileStream(file)
    lexer = SetlXgrammarLexer(input)
    stream = CommonTokenStream(lexer)
    parser = SetlXgrammarParser(stream)
    tree = parser.block()
    if parser.getNumberOfSyntaxErrors() > 0:  # TODO better error handling
        return
    state = SetlxState()
    body = tree.blk.to_python(state)
    body = state.imports.to_python(state) + body
    code = ast.Module(body=body)
    return code
