from antlr4.error.ErrorListener import ErrorListener
import sys
import json
from antlr4 import FileStream,CommonTokenStream
from grammar.setlx.antlr.SetlXgrammarParser import SetlXgrammarParser
from grammar.setlx.antlr.SetlXgrammarLexer import SetlXgrammarLexer
from grammar.setlx.antlr.SetlXgrammarListener import SetlXgrammarListener
from var_dump import var_dump

from grammar.setlx.state import SetlxState

def main(argv):
    input = FileStream(argv[1])
    lexer = SetlXgrammarLexer(input)
    stream = CommonTokenStream(lexer)
    parser = SetlXgrammarParser(stream)
    lexer = SetlXgrammarParser(stream)
    tree = parser.block()
    if parser.getNumberOfSyntaxErrors() > 0: # TODO better error handling
        return
    # var_dump(tree.blk.to_python(state))
    print(tree.blk.to_python(SetlxState()).to_code())


if __name__ == '__main__':
    main(sys.argv)
