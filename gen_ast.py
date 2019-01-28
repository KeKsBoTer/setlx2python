import astor
import sys

def main(argv):
    ast = astor.dump_tree(astor.parse_file(argv[1]))
    print(ast)


if __name__ == '__main__':
    main(sys.argv)
