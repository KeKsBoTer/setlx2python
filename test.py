from antlr4.error.ErrorListener import ErrorListener
import sys
import json
from antlr4 import FileStream, CommonTokenStream
from grammar.setlx.antlr.SetlXgrammarParser import SetlXgrammarParser
from grammar.setlx.antlr.SetlXgrammarLexer import SetlXgrammarLexer
from grammar.setlx.antlr.SetlXgrammarListener import SetlXgrammarListener
# from var_dump import var_dump
from transpiler import Transpiler
import astor
import ast


def main(argv):
    if argv[1] == "ast":
        input = FileStream(argv[2]+".stlx")
        lexer = SetlXgrammarLexer(input)
        stream = CommonTokenStream(lexer)
        parser = SetlXgrammarParser(stream)
        t = Transpiler(parser)
        code = t.transpile()
        print(astor.dump_tree(code))
        py_file = open(argv[2]+".py")
        print("\n############# from file #################\n")
        print(astor.dump_tree(ast.parse(py_file.read())))
        py_file.close()
    elif argv[1] == "run":
        input = FileStream(argv[2])
        lexer = SetlXgrammarLexer(input)
        stream = CommonTokenStream(lexer)
        parser = SetlXgrammarParser(stream)
        t = Transpiler(parser)
        code = astor.to_source(t.transpile())
        print(code)
        print("\n###### executing generated code ########")
        exec(code, {})
    else:
        raise f"unknown command {argv[1]}, use 'ast' or 'run'"


if __name__ == '__main__':
    main(sys.argv)
