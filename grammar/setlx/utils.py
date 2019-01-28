import grammar.python.statements as py_stmnt
import grammar.python.types as py_type


def iterator_from_chain(state, iter_chain):
    # add import for list product
    state.imports.add("itertools", "product")

    assignables = [i.assignable.to_python(
        state) for i in iter_chain]
    assignable = py_type.PyList(py_type.ExplicitList(assignables))

    exprs = [e.expression.to_python(state) for e in iter_chain]
    list_product = py_stmnt.FunctionCall(
        py_type.Variable("product"), exprs)

    return py_stmnt.PyIterator(assignable, list_product)


def call_function(name, params):
    return py_stmnt.FunctionCall(py_type.Variable(name), params)


def to_python(state, objects):
    return [x.to_python(state) for x in objects]
