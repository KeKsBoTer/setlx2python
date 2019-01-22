
class Block:
    Indent = 4 * " "

    def __init__(self, stmnts):
        self.stmnts = stmnts

    def to_code(self, indent=0):
        stmnts = [indent * Block.Indent + # indent before line
                  s.to_code(indent+1) for s in self.stmnts]
        return "\n".join(stmnts)
