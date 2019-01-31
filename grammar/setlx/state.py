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

    def add(self, module, obj):
        mod = [i for i in self.imports if i.module == module]
        if len(mod) > 0:
            names = [n for n in mod[0].names if n.name == obj]
            if len(names) == 0:
                mod[0].names.append(ast.alias(name=obj, asname=None))
        else:
            # use set to eliminates doubles
            self.imports.append(ast.ImportFrom(module=module, names=[
                                ast.alias(name=obj, asname=None)], level=0))

    def to_python(self, state):
        return self.imports
