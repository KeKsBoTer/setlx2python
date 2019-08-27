import ast
from collections import namedtuple
from setlx.built_ins import built_ins


class ImportList:
    """ A Class to keep track of all the required imports"""
    def __init__(self):
        """ list of modules that need to be imported"""
        self.imports = []

    def add(self, module: str):
        """ add a module to the list of required modules """
        if module not in self.imports:
            self.imports.append(module)

    def to_python(self, state) -> list:
        """ Generates the python import statements based on the list of imports """
        return [ast.Import(names=[ast.alias(name=i, asname=None)]) for i in self.imports]


class ClassContext:
    """ The context object for the state in which all information about a class is storred """
    def __init__(self,id):
        """ the name of the class """
        self.id = id
        """ list of class validattribtues """
        self.variables = []
        
        """ indicates if the transpiler is currently in the static part of the class """
        self.static = False


class TranspilerState:
    """ The state of the transpiler, keeps track of all needed information """
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

    def is_class_static(self) -> bool:
        """ checks if the transpiler is in the static part of a class """
        return self.class_context != None and self.class_context.static == True

    def is_class_variable(self,id: str) -> bool:
        """ checks whether a given variable of the current class """
        return self.class_context != None and id in self.class_context.variables

    def check_built_ins(self, id: str):
        """ removes function from built_ins if it is overriden in the code """
        if id in self.built_ins:
            del self.built_ins[self.built_ins.index(id)]
