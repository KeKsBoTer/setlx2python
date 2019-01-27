import grammar.python.statements as py_stmt


class SetlxState:
    def __init__(self):
        # current statement
        self.statement = None
        self.before_stmnts = []
        self.procedure_counter = 0
        self.level = 0
        self.imports = ImportList()


class ImportList:
    def __init__(self):
        self.imports = []

    def add(self, module, obj):
        mod = [i for i in self.imports if i.module == module]
        if len(mod) > 0:
            mod[0].objects.add(obj)
        else:
            # use set to eliminates doubles
            self.imports.append(py_stmt.Import(module, set([obj])))

    def to_code(self, indent=0):
        imports = [i.to_code(indent) for i in self.imports]
        return "\n".join(imports)
