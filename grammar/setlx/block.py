
import grammar.python.block as py
import ast

class Block:
    def __init__(self,stmnts):
        self.stmnts = stmnts

    def to_python(self, state):
        procedure_counter = state.procedure_counter
        state.procedure_counter = 0
        """
        stmnts = []
        for s in self.stmnts:
            level = state.level
            state.level+=1 # next depth level
            stmnt = s.to_python(state)
            state.level = level

            if len(state.before_stmnts) > 0:
                # prepend statements that need to be executed before statement (e.g. function declaration)
                before, not_before = [], []
                for x in state.before_stmnts:
                    (not_before, before)[x.level > state.level].append(x) # only append before statements that were generated in higher levels

                stmnts += before
                state.before_stmnts = not_before

            stmnts.append(stmnt)
        
        state.procedure_counter = procedure_counter
        # return py.Block(stmnts)
        """
        stmnts = [x.to_python(state) for x in self.stmnts]
        mod = ast.Module(body=stmnts)
        return mod