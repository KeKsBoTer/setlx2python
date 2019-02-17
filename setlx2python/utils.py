import ast


def call_function(name, params):
    return ast.Call(func=ast.Name(id=name), args=params, keywords=[])


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
            stmnt.decorator_list = [
                ast.Name(id="staticmethod")] + stmnt.decorator_list
