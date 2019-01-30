from grammar.setlx.state import SetlxState
import ast


class Transpiler:
    def __init__(self, parser):
        self.parser = parser

    def transpile(self):
        tree = self.parser.block()
        if self.parser.getNumberOfSyntaxErrors() > 0:  # TODO better error handling
            return
        state = SetlxState()
        body = tree.blk.to_python(state)
        body = state.imports.to_python(state) + body
        code = ast.Module(body=body)
        return code
