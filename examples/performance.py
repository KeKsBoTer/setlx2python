import os
from sys import argv
import time
import subprocess


def loadTestSnippets(path):
    module_dir = os.path.dirname(__file__)
    tests_dir = os.path.join(module_dir, path)
    print(tests_dir)
    files = os.listdir(path=tests_dir)
    setlx_files = [f for f in files if f.endswith(".stlx")]
    py_files = [f for f in files if f.endswith(".py")]

    missing = [f for f in setlx_files if f[:-5]+".py" not in py_files]

    #assert len(missing) == 0, f"missing python files for {', '.join(missing)}"

    tests = [(f, f[:-5]+".py") for f in setlx_files]
    if len(argv[1:]) > 0:
        tests = [(f_stlx, f_py)
                 for (f_stlx, f_py) in tests if f_stlx[:-5] in argv[1:]]

    return [(os.path.join(tests_dir, t[0]), os.path.join(tests_dir, t[1])) for t in tests]


def measure():
    algo_path = "algorithms"
    file_paths = loadTestSnippets(algo_path)
    times = []
    with open("times.csv", "w+") as f:
        f.write("setlx file, setlx time, py file, py time \n")
        for setlx_f, py_f in file_paths[:20]:
            if "legendre" in setlx_f or "tic" in setlx_f:
                continue
            # python
            start = time.perf_counter()
            cmd = f"python {py_f}".replace("-", "_")
            code_py = os.system(cmd)
            py_time = time.perf_counter() - start
            if code_py != 0:
                continue
            # setlx
            start = time.perf_counter()
            cmd = f"setlx {setlx_f}"
            code_stlx = os.system(cmd)
            setlx_time = time.perf_counter() - start
            if (code_stlx != 0):
                continue
            backslash = '\\'
            f.write(
                f"{setlx_f.split(backslash)[-1]},{py_time}s,{py_f.split(backslash)[-1]},{setlx_time}s\n")
            f.flush()


measure()
