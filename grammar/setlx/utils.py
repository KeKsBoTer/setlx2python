import ast


def iterator_from_chain(state, iter_chain):
    if len(iter_chain) == 1:
        return to_python(state, [iter_chain[0].assignable, iter_chain[0].expression])
    # add import for list product
    state.imports.add("itertools", "product")

    assignables = [i.assignable.to_python(
        state) for i in iter_chain]
    assignable = ast.List(elts=assignables)

    exprs = [e.expression.to_python(state) for e in iter_chain]
    list_product = call_function("product", exprs)

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
    state.imports.add("copy", "deepcopy")
    call = call_function("deepcopy",[param])
    return ast.Assign([param], call)