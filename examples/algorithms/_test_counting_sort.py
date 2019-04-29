import setlx
from counting_sort import *


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
    setlx.print('\nSorted List:')
    [SortedNames, SortedGrades] = countingSort(Names, Grades)
    for i in setlx.List(setlx._range(1, len(Lines))):
        setlx.print(f'{SortedNames[i]}: {SortedGrades[i]}')


def fillNames(Names):
    [Names] = setlx.copy([Names])
    maxLength = setlx.max(setlx.List([len(s) for s in Names]))
    return setlx.List([(s + ' ' * (maxLength + 1 - len(s))) for s in Names])


main()
