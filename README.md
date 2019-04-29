# setlx2python - Convert setlx code to python

setlx2python is a tool that compiles [SetlX](https://randoom.org/Software/SetlX/)-Code to Python 3 code. The generated code is of good readability and ready to run most of the times. Sometimes small manual adjustments are needed to make the code runable.

# Not supported SetlX-Features
Some features of the lanugage SetlX are not supported:
- scan
- terms
- term matching
- some native functions
  - la_pseudoInverse
  - la_svd
  - la_solve
  - la_eigenValues
  - la_eigenVectors
  - la_hadamard
  - nextProbablePrime
  - rational
  - trace
  
## Installation
Clone the repository and run the following comand in the directory.
```
pip install -e <path_to_directory>
```
To run the generated SetlX-Code you also need to install the [setlpy](https://github.com/daniel-scholz/setlpy) package for python.


## How to use
```
$ setlx2python
Usage:
  setlx2python <file> [-c <output>]
  setlx2python -h | --help
  setlx2python --version
```
For more information about the usage just write `setlx2python -h`
