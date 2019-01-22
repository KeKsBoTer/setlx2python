
import grammar.python.block as py

class Block:
    def __init__(self,stmnts):
        self.stmnts = stmnts

    def to_python(self):
        return py.Block([s.to_python() for s in self.stmnts])