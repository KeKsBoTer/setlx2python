import setlx


@setlx.procedure
def isRightOf(h1, h2):
    return h1 == h2 + 1


@setlx.procedure
def nextTo(h1, h2):
    return setlx.abs(h1 - h2) == 1


@setlx.procedure
def zebraPuzzle():
    first = 1
    middle = 3
    result = setlx.Set()
    orderings = setlx.permutations(setlx.List(setlx._range(1, 5)))
    for [red, green, ivory, yellow, blue] in orderings:
        if isRightOf(green, ivory):
            for [english, spaniard, ukrainian, japanese, norwegian] in orderings:
                if (english == red and norwegian == first) and nextTo(norwegian, blue):
                    for [coffee, tea, milk, orange, water] in orderings:
                        if (coffee == green and ukrainian == tea) and milk == middle:
                            for [gold, kools, west, luckies, camel] in orderings:
                                if (kools == yellow and luckies == orange) and japanese == camel:
                                    for [dog, snails, fox, horse, zebra] in orderings:
                                        if ((spaniard == dog and gold == snails) and nextTo(west, fox)) and nextTo(kools, horse):
                                            setlx.print(f'colors:        {setlx.List([red, green, ivory, yellow, blue])}')
                                            setlx.print(f'nationalities: {setlx.List([english, spaniard, ukrainian, japanese, norwegian])}')
                                            setlx.print(f'drinks:        {setlx.List([coffee, tea, milk, orange, water])}')
                                            setlx.print(f'pet:           {setlx.List([dog, snails, fox, horse, zebra])}')
                                            setlx.print(f'cigarettes:    {setlx.List([gold, kools, west, luckies, camel])}')
                                            result += setlx.Set([setlx.List([water, zebra])])
    return result


setlx.print(zebraPuzzle())

