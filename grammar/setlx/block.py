
import grammar.python.block as py

class Block:
    def __init__(self,stmnts):
        self.stmnts = stmnts

    def to_python(self, state):
        procedure_counter = state.procedure_counter
        state.procedure_counter = 0

        stmnts = []
        for s in self.stmnts:
            stmnt = s.to_python(state)

            if len(state.before_stmnts) > 0:
                # prepend statements that need to be executed before statement (e.g. function declaration)
                stmnts += state.before_stmnts
                state.before_stmnts = []

            stmnts.append(stmnt)
        
        state.procedure_counter = procedure_counter
        return py.Block(stmnts)