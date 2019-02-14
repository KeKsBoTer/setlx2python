import ast


def iterator_from_chain(state, iter_chain):
    if len(iter_chain) == 1:
        return to_python(state, [iter_chain[0].assignable, iter_chain[0].expression])

    assignables = [i.assignable.to_python(
        state) for i in iter_chain]
    assignable = ast.List(elts=assignables)

    exprs = [e.expression.to_python(state) for e in iter_chain]
    list_product = setlx_function(state, "cartesian_product", exprs)

    return [assignable, list_product]


def call_function(name, params):
    return ast.Call(func=ast.Name(id=name), args=params, keywords=[])


def to_python(state, objects):
    return [x.to_python(state) for x in objects]


def bool_true():
    return ast.NameConstant(value=True)


def bool_false():
    return ast.NameConstant(value=False)


def deep_copy_param(param, state):
    call = setlx_function(state, "deepcopy", [param])
    return ast.Assign([param], call)


def setlx_access(state, name):
    state.imports.add("setlx")
    return ast.Attribute(value=ast.Name(id="setlx"), attr=name)


def setlx_function(state, name, args):
    state.imports.add("setlx")
    return ast.Call(func=setlx_access(state, name), args=args, keywords=[])


def unpack_error(state, target):
    state.imports.add("setlx")
    unpack_call = setlx_function(state, "unpack_error", [ast.Name(id='e')])
    return ast.Assign(targets=[ast.Name(id=target)], value=unpack_call)


def make_funcs_static(block):
    for stmnt in block:
        if isinstance(stmnt, ast.FunctionDef):
            stmnt.decorator_list = ["staticmethod"] + stmnt.decorator_list


def add_self(funcs):
    for f in funcs:
        f.args.args = [ast.arg(arg='self', annotation=None)]+f.args.args
