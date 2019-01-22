class SetlxState:
    def __init__(self):
        # current statement
        self.statement = None
        self.before_stmnts = []
        self.procedure_counter = 0