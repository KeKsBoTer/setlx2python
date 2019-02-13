from sys import argv, stdout
import os
import subprocess
import ast
import astor
import difflib
import colorama
import traceback
from transpiler import transpile
from termcolor import cprint


def _unidiff_output(expected, actual):
    """
    Helper function. Returns a string containing the unified diff of two multiline strings.
    """

    expected = expected.splitlines(1)
    actual = actual.splitlines(1)

    diff = difflib.unified_diff(expected, actual)
    print
    return ''.join(diff)


class WritableObject:
    def __init__(self):
        self.content = ""

    def write(self, string):
        self.content += string


colorama.init()

module_dir = os.path.dirname(__file__)
tests_dir = os.path.join(module_dir, "tests")

flags = [f[2:] for f in argv[1:] if f[0:2] == "--"]
argv = [a for a in argv if a[2:] not in flags]

files = os.listdir(path=tests_dir)
setlx_files = [f for f in files if f.endswith(".stlx")]
py_files = [f for f in files if f.endswith(".py")]

missing = [f for f in setlx_files if f[:-5]+".py" not in py_files]

if len(missing) > 0:
    cprint(f"missing python files for {', '.join(missing)}", 'red')
    exit(2)

tests = [(f, f[:-5]+".py") for f in setlx_files]
if len(argv[1:]) > 0:
    tests = [(f_stlx, f_py)
             for (f_stlx, f_py) in tests if f_stlx[:-5] in argv[1:]]

print(f"running tests: {', '.join([f[0][:-5] for f in tests])}")

for test in tests:
    successfull = True
    try:
        gen_tree = transpile(os.path.join(tests_dir, test[0]))
    except Exception as e:
        cprint(f"ERROR: cannot transpile {test[0]}", "red")
        cprint(str(e), "red")
        cprint("".join(traceback.format_tb(e.__traceback__, limit=-4)), "red")
        continue
    with open(os.path.join(tests_dir, test[1])) as f:
        py_code = f.read()
    py_tree = ast.parse(py_code)

    gen_ast = astor.dump_tree(gen_tree)
    py_ast = astor.dump_tree(py_tree)
    code = None
    try:
        code = astor.to_source(gen_tree)
    except Exception as e:
        cprint(f"ERROR: invalid generated ast for {test[0]}", "red")
        cprint(str(e), "red")
        cprint("".join(traceback.format_tb(e.__traceback__, limit=-4)), "red")
        successfull = False

    output = WritableObject()
    if code != None:
        try:
            sprint = lambda *objects, sep=' ', end='\n', file=stdout, flush=False: print(
                *objects, sep=sep, end=end, file=output, flush=flush)
            exec(code, {"print": sprint})
        except Exception as e:
            output.write(str(e)+"\n")
            output.write(
                "".join(traceback.format_tb(e.__traceback__, limit=-4)))
            # continue

    if gen_ast != py_ast:
        cprint(
            f"WARNING: generated ast does not match py file ({test[0][:-5]})", "yellow")
        if "ast" in flags:
            print("-"*5+"generated"+"-"*5)
            print(gen_ast)
            print("-"*5+"expected"+"-"*5)
            print(py_ast)

        if "diff" in flags:
            print(f'{"#"*5} generated <> {test[1]} {"#"*5}')
            print(_unidiff_output(py_ast, gen_ast))
    elif "ast" in flags:
        print("-"*10+"generated"+"-"*10)
        print(gen_ast)

    if "code" in flags:
        print(f'{"#"*10} generated code {"#"*10}')
        print(code)

    if "output" in flags:
        print(f"{'#'*10} output {'#'*10}")
        print(output.content)

    if successfull:
        cprint(f"INFO: {test[0][:-5]} was successfull", 'green')
