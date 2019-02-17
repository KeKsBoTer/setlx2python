import astor
import ast
import sys

def main(argv):
    tree = astor.dump_tree(ast.parse(argv[1]))
    print(tree)


if __name__ == '__main__':
    main(sys.argv)
