import ast
import astor
import sys

input = str(sys.stdin.readlines())

print(astor.dump_tree(ast.parse(input)))