
from unittest import TestCase
from sys import argv, stdout
import os
import ast
import sys
import astor
import pytest
from setlx2python.cli import transpile
import warnings


def loadTestSnippets(path):
    module_dir = os.path.dirname(__file__)
    tests_dir = os.path.join(module_dir, path)

    files = os.listdir(path=tests_dir)
    setlx_files = [f for f in files if f.endswith(".stlx")]
    py_files = [f for f in files if f.endswith(".py")]

    missing = [f for f in setlx_files if f[:-5]+".py" not in py_files]

    assert len(missing) == 0, f"missing python files for {', '.join(missing)}"

    tests = [(f, f[:-5]+".py") for f in setlx_files]
    if len(argv[1:]) > 0:
        tests = [(f_stlx, f_py)
                 for (f_stlx, f_py) in tests if f_stlx[:-5] in argv[1:]]

    return [(os.path.join(tests_dir, t[0]), os.path.join(tests_dir, t[1])) for t in tests]


def gen_code(setlx_file, py_file):

    try:
        gen_tree = transpile(setlx_file)
    except Exception as e:
        TestCase.fail(f"cannot transpile {setlx_file}:{str(e)}")

    with open(py_file) as f:
        py_code = f.read()
    py_tree = ast.parse(py_code)

    gen_ast = astor.dump_tree(gen_tree)
    py_ast = astor.dump_tree(py_tree)

    if gen_ast != py_ast:
        warnings.warn(Warning(
            f"generated ast from {os.path.basename(setlx_file)} does not match py file ({os.path.basename(py_file)})"))
    code = None
    try:
        code = astor.to_source(gen_tree)
    except Exception as e:
        TestCase.fail(
            f"ERROR: invalid generated ast for {setlx_file}:{str(e)}")
    return (code, gen_ast, py_ast)


def no_print(*objects, sep=' ', end='\n', file=stdout,
             flush=False): pass  # do not print


def no_exit(): pass  # do not exit


@pytest.mark.parametrize('files', loadTestSnippets("snippets"))
def test_snippet(files):
    TestCase.maxDiff = None

    with warnings.catch_warnings(record=True) as w:
        (code, ast_setlx, ast_py) = gen_code(files[0], files[1])
        TestCase.assertEqual(TestCase(),ast_setlx, ast_py)

    try:
        exec(code, {"print": no_print, "exit": no_exit})
    except AssertionError as e:
        pass
    except Exception as e:
        # print code with line numbers
        print("\n".join([f"{n+1}:  {line}" for n,
                         line in enumerate(code.split("\n"))]))
        raise e
