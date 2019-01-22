from antlr4.error.ErrorListener import ErrorListener
import sys
import json
from antlr4 import *
from grammar.setlx.antlr.SetlXgrammarParser import SetlXgrammarParser
from grammar.setlx.antlr.SetlXgrammarLexer import SetlXgrammarLexer
from grammar.setlx.antlr.SetlXgrammarListener import SetlXgrammarListener
from var_dump import var_dump


def main(argv):
    input = FileStream(argv[1])
    lexer = SetlXgrammarLexer(input)
    stream = CommonTokenStream(lexer)
    parser = SetlXgrammarParser(stream)
    lexer = SetlXgrammarParser(stream)
    tree = parser.block()
    if parser.getNumberOfSyntaxErrors() > 0: # TODO better error handling
        return
    # var_dump(tree.blk.to_python())
    print(tree.blk.to_python().to_code())


if __name__ == '__main__':
    main(sys.argv)
