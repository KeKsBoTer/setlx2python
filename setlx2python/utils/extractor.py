import inspect
import sys

import grammar.setlx.block as block
import grammar.setlx.statements as stmnts
import grammar.setlx.types as types
classes = []
for mod in [block,stmnts,types]:
    classes += inspect.getmembers(sys.modules[mod.__name__], inspect.isclass)
classes = list(set(classes))
classes.sort(key=lambda tup: tup[0])

print("from collections import namedtuple as nt")
for name, c in classes:
    init_info = inspect.getfullargspec(getattr(c,"__init__"))
    print(f"{name} = nt('{name}',{init_info.args[1:]})")
