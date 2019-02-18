import re
import inspect
import setlx2python.grammar.types as types

with open("setlx2python/grammar/SetlXgrammar.g4","r") as f:
    grammar = f.read()
    nodes = re.findall(r"[^\w]([A-Z]\w+)\(",grammar)
    #print(nodes)
    names = [n for n in dir(types)]
    print([n for n in nodes if n not in names])