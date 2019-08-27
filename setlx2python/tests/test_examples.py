
import ast
import glob
import os
import subprocess
import sys
import tempfile
import warnings
from io import StringIO
from unittest import TestCase

import astor
import pytest

import setlx
from setlx2python.cli import transpile
from setlx2python.transpiler import NotSupported


def loadTestCode(path):
    module_dir = os.path.dirname(__file__)
    tests_dir = os.path.join(module_dir, path)

    py_path = os.path.join(tests_dir, '**/*.stlx')

    files = glob.glob(py_path, recursive=True)

    return files


@pytest.mark.parametrize('file', loadTestCode("examples"))
@pytest.mark.timeout(120)
def test_snippet(file):

    TestCase.maxDiff = None
    dirname = os.path.dirname(file)

    try:
        py_code = transpile(file, is_string=False)
    except NotSupported as e:
        pytest.skip(f"{file}: {str(e)}")
    except SyntaxError as e:
        pytest.fail(f"{file}: {str(e)}")

    p = subprocess.Popen(["setlx", file], stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE, cwd=dirname)
    return_code = p.wait(120)
    if return_code != 0:
        pytest.skip(f"{file}: setlx program exited with code {return_code}")
    setlx_output = p.stdout.read().decode("utf-8")
    p.kill()

    with tempfile.NamedTemporaryFile("w", delete=True) as f:
        f.write(py_code)
        f.seek(0, 0)
        p = subprocess.Popen(
            ["python3", f.name], stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd=dirname)
        p.wait(120)
        python_output = p.stdout.read().decode("utf-8")
        python_err = p.stderr.read().decode("utf-8")
        p.kill()
        if "ModuleNotFoundError" in python_err:
            pytest.skip(python_output)

    TestCase.assertEqual(TestCase(), setlx_output, python_output)
