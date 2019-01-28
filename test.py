from antlr4.error.ErrorListener import ErrorListener
import sys
import json
from antlr4 import FileStream, CommonTokenStream
from grammar.setlx.antlr.SetlXgrammarParser import SetlXgrammarParser
from grammar.setlx.antlr.SetlXgrammarLexer import SetlXgrammarLexer
from grammar.setlx.antlr.SetlXgrammarListener import SetlXgrammarListener
# from var_dump import var_dump
from transpiler import Transpiler


def main(argv):
    input = FileStream(argv[1])
    lexer = SetlXgrammarLexer(input)
    stream = CommonTokenStream(lexer)
    parser = SetlXgrammarParser(stream)
    t = Transpiler(parser)
    code = t.transpile()
    print(code)
    print("\n###### executing generated code ########")
    exec(code, {})


if __name__ == '__main__':
    main(sys.argv)
