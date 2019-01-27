from grammar.setlx.state import SetlxState

class Transpiler:
    def __init__(self,parser):
        self.parser = parser

    def transpile(self):
        tree = self.parser.block()
        if self.parser.getNumberOfSyntaxErrors() > 0: # TODO better error handling
            return
        state = SetlxState()
        code = tree.blk.to_python(state).to_code()
        imports = state.imports.to_code()
        return f"{imports}\n{code}"