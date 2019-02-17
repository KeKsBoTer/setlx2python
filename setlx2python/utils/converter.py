import inspect
import sys

import grammar.setlx.block as block
import grammar.setlx.statements as stmnts
import grammar.setlx.types as types

classes = []
for mod in [block, stmnts, types]:
    classes += inspect.getmembers(sys.modules[mod.__name__], inspect.isclass)
classes.sort(key=lambda tup: tup[0])

for name, c in set(classes):
    to_python = getattr(c, "to_python") if "to_python" in dir(c) else None
    init_info = inspect.getfullargspec(getattr(c, "__init__"))

    #print(f"{name} = nt('{name}',{init_info.args[1:]})")

    if to_python != None:
        to_python_info = inspect.getfullargspec(to_python)
        code = inspect.getsource(to_python)
        code = code.replace("self.", "")
        code = code.replace("state", "self.state")
        code = code.split("\n")[1:]
        nl = "\n"
        print(
            f"def {name.lower()}(self, {', '.join(init_info.args[1:])}):{nl}{nl.join(code)}")
