import setlx


def graph2Dot(Parent, file):
    [Parent, file] = setlx.copy([Parent, file])
    setlx.print(Parent)
    graph = 'digraph G {\n'
    graph += '    ordering = out;\n'
    graph += '    node [shape = record];\n'
    graph += '    edge [dir   = back  ];\n'
    count = 0
    M = setlx.Set([x for [x, _] in Parent]) + setlx.Set([p for [_, p] in Parent])
    for p in M:
        CL = children(p, Parent)
        if CL != setlx.Set():
            graph += f'    n{p} -> ' + setlx.join(setlx.List([f'n{x}' for x in CL]), ',')
            graph += ';\n'
    for x in M:
        graph += f'    n{x} [label = \\"{x}\\"];\n'
    graph += '}\n'
    setlx.writeFile(f'{file}.dot', setlx.List([graph]))
    setlx.run(f'dot -Tpdf {file}.dot -o {file}.pdf')
    setlx.run(f'open {file}.pdf')


def children(x, Parent):
    [x, Parent] = setlx.copy([x, Parent])
    return setlx.Set([y for [y, p] in Parent if p == x])
