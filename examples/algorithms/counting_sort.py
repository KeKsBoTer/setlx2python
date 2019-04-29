import setlx


def countingSort(Names, Grades):
    [Names, Grades] = setlx.copy([Names, Grades])
    assert len(Names) == len(Grades), f'{len(Names)} != {len(Grades)}'
    maxGrade = setlx.max(Grades)
    Counts = setlx.List([0]) * maxGrade
    Indices = setlx.List()
    SortedNames = setlx.List()
    SortedGrades = setlx.List()
    for g in Grades:
        Counts[g] += 1
    Indices[1] = 1
    for g in setlx.List(setlx._range(2, maxGrade)):
        Indices[g] = Indices[g - 1] + Counts[g - 1]
    for i in setlx.List(setlx._range(1, len(Names))):
        g = Grades[i]
        index = Indices[g]
        SortedNames[index] = Names[i]
        SortedGrades[index] = Grades[i]
        Indices[g] += 1
    return setlx.List([SortedNames, SortedGrades])
