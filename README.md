# setlx2python - Convert setlx code to python

## Installation
```
pip install git+https://github.com/KeKsBoTer/setlx2python.git
```

## How to use
```
$ setlx2python
Usage:
  setlx2python <file>
  setlx2python -h | --help
  setlx2python --version
```
# TODO
Simon:
- support file loading
- recognize lambda functions as class functions (see heap.stlx)
- support f_str as __str__ method
- no None (om) in Lists!
- make tic-tac-toe work

Daniel:
- fix "could not delete {1}" in union_find_naive.py
- union_find_oo.py: R is missing element [1,9] (line 42) (wrong map behaviour)
- merge_sort_array.py line 75 assertion fails, but shouldn't 

# Features that will not be supported
- execute / eval
- scan
- terms
- term matching