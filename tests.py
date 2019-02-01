from sys import argv
import os
from transpiler import transpile


module_dir = os.path.dirname(__file__)
tests_dir = os.path.join(module_dir, "tests/code")


files = os.listdir(path=tests_dir)
setlx_files = [f for f in files if f.endswith(".stlx")]
py_files = [f for f in files if f.endswith(".py")]

missing = [f for f in setlx_files if f[:-5]+".py" not in py_files]

if len(missing) > 0:
    print(f"missing python files for {', '.join(missing)}")
    exit(2)


tests = setlx_files if len(argv[1:]) == 0 else [
    f for f in setlx_files if f[:-5] in argv[1:]]

print(f"running tests: {', '.join([f[:-5] for f in tests])}")

for test in zip(setlx_files, py_files):
    try:
        ast = transpile(os.path.join(tests_dir, test[0]))
    except Exception as e:
        print(f"ERROR: cannot transpile {test[0]}")
        #print(e)
