"""
setlx2python
 
Usage:
  setlx2python [--c] <file> [-o <output>] 
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
import astor

from antlr4 import FileStream, InputStream

from setlx2python.transpiler import Transpiler, NotSupported, parse_input
from . import __version__ as VERSION


def transpile(file: str, is_string: bool) -> ast.Module:
    """ translates a given setlx file to a python string

    Parameters
    ----------
    file : str
        The path to the setlx file

    """
    if not is_string:
        input = FileStream(file, encoding="utf-8")
    else:
        input = InputStream(file)

    try:
        parser = parse_input(input)
        tree = parser.block()
        t = Transpiler(tree.blk)
        body = t.transpile()
    except (NotSupported, SyntaxError) as e:
        print(e, file=sys.stderr)
        sys.exit(2)

    code = ast.Module(body=body)
    return code


def pretty_source(source):
    """ Prettify the source.
    """
    return ''.join(source)


def main():
    options = docopt(__doc__, version=VERSION)

    # CLI parameters
    input_file = options["<file>"]
    output_file = options["<output>"]

    python_ast = transpile(input_file, options["--c"])
    code = astor.to_source(python_ast, pretty_source=pretty_source)
    if options["-o"]:
        with open(output_file, "w") as f:
            f.write(code)
    else:
        print(code)
