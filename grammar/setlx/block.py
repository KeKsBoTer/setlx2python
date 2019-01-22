
import grammar.python.block as py

class Block:
    def __init__(self,stmnts):
        self.stmnts = stmnts

    def to_python(self, state):
        procedure_counter = state.procedure_counter
        state.procedure_counter = 0

        stmnts = [s.to_python(state) for s in self.stmnts]
        if len(state.before_stmnts) > 0:
            # prepend statements that need to be executed before statement (e.g. function declaration)
            stmnts = state.before_stmnts + stmnts 
            state.before_stmnts = []
        
        state.procedure_counter = procedure_counter
        return py.Block(stmnts)