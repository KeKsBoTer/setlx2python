"""
setlx2python
 
Usage:
  setlx2python <file>
  setlx2python -h | --help
  setlx2python --version
 
Options:
  -h --help                         Show this screen.
  --version                         Show version.
 
Examples:
  setlx2python hello.stlx
 
Help:
  For help using this tool, please open an issue on the Github repository:
  https://github.com/KeKsBoTer/setlx2python
"""

import ast
import sys
from docopt import docopt
from astor import to_source, string_repr

from antlr4 import FileStream

from setlx2python.transpiler import Transpiler, NotSupported, parse_input
from . import __version__ as VERSION


def transpile(file):
    input = FileStream(file, encoding="utf-8")
    parser = parse_input(input)
    tree = parser.block()
    t = Transpiler(tree.blk)
    try:
        body = t.transpile()
    except (NotSupported, SyntaxError) as e:
        print(e)
        sys.exit(2)

    code = ast.Module(body=body)
    return code


def pretty_source(source):
    """ Prettify the source.
    """
    # TODO we should split somewhere
    return ''.join(source)


def main():
    options = docopt(__doc__, version=VERSION)
    ast_tree = transpile(options["<file>"])
    print(to_source(ast_tree, pretty_source=pretty_source))
