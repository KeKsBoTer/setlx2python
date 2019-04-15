import setlx
setlx.load('counting-sort.stlx')


@setlx.procedure
def main():
    Lines = setlx.readFile('counting-sort-data.txt')
    Names = setlx.List()
    Grades = setlx.List()
    for i in setlx.List(setlx._range(1, len(Lines))):
        [Names[i], Grades[i]] = setlx.split(Lines[i], ',')
        Grades[i] = setlx.int(Grades[i])
    Names = fillNames(Names)
    for i in setlx.List(setlx._range(1, len(Lines))):
        setlx.print(f'{Names[i]}: {Grades[i]}')
    setlx.print('\\nSorted List:')
    [SortedNames, SortedGrades] = countingSort(Names, Grades)
    for i in setlx.List(setlx._range(1, len(Lines))):
        setlx.print(f'{SortedNames[i]}: {SortedGrades[i]}')


@setlx.procedure
def fillNames(Names):
    maxLength = setlx.max(setlx.List([len(s) for s in Names]))
    return setlx.List([(s + ' ' * (maxLength + 1 - len(s))) for s in Names])


main()

