import ast


class SetlxState:
    def __init__(self):
        # current statement
        self.before_stmnts = []
        self.procedure_counter = 0
        # scope level
        self.level = 0
        # modules that need to be imported
        self.imports = ImportList()


class ImportList:
    def __init__(self):
        self.imports = []

    def add(self, module):
        if module not in self.imports:
            self.imports.append(module)

    def to_python(self, state):
        return [ast.Import(names=[ast.alias(name=i, asname=None)]) for i in self.imports]
