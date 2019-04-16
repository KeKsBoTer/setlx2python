import ast
from collections import namedtuple
from setlx import built_ins


class ImportList:
    def __init__(self):
        self.imports = []

    def add(self, module):
        if module not in self.imports:
            self.imports.append(module)

    def to_python(self, state):
        return [ast.Import(names=[ast.alias(name=i, asname=None)]) for i in self.imports]


class ClassContext:
    def __init__(self,id):
        self.id = id
        self.variables = []
        self.static = False


class TranspilerState:
    def __init__(self):
        # a function that allows to add a statement before the current one
        self.add_before = None

        # number of procedures in this block
        self.procedure_counter = 0

        # scope level
        self.level = 0

        # modules that need to be imported
        self.imports = ImportList()

        # a list of all valid variables
        self.variables = []

        # track all valid procedures
        self.procedures = {}

        # keep track of all valid built in functions
        self.built_ins = built_ins

        # the class the transpiler is currently in. None if it is in no class
        self.class_context = None

    def is_class_static(self):
        return self.class_context != None and self.class_context.static == True

    def is_class_variable(self,id):
        return self.class_context != None and id in self.class_context.variables

    def check_built_ins(self, id):
        # remove function from built_ins if it is overriden in the code
        if id in self.built_ins:
            del self.built_ins[self.built_ins.index(id)]
