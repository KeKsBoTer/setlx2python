"""
setlx2python
 
Usage:
  setlx2python [-c] <file>
  setlx2python -h | --help
  setlx2python --version
 
Options:
  -h --help                         Show this screen.
  --version                         Show version.
  -c                                File is code
 
Examples:
  setlx2python hello.stlx
  setlx2python -c "print(5!);"
 
Help:
  For help using this tool, please open an issue on the Github repository:
  https://github.com/KeKsBoTer/setlx2python
"""

import ast
import sys
from docopt import docopt
from astor import to_source, string_repr

from antlr4 import FileStream, InputStream

from setlx2python.transpiler import Transpiler, NotSupported, parse_input
from . import __version__ as VERSION


def transpile(file=None, code=None):
    if code != None:
        input = InputStream(code)
    elif file != None:
        input = FileStream(file, encoding="utf-8")
    else:
        raise Exception("no file or code provided")
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
    if options["-c"]:
        ast_tree = transpile(code=options["<file>"])
    else:
        ast_tree = transpile(file=options["<file>"])

    print(to_source(ast_tree, pretty_source=pretty_source))
