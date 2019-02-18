import setlx


@setlx.procedure
def isRightOf(h1, h2):
    return h1 == h2 + 1


@setlx.procedure
def nextTo(h1, h2):
    return abs(h1 - h2) == 1


@setlx.procedure
def zebraPuzzle():
    first = 1
    middle = 3
    result = set()
    orderings = permutations(list(range(1, 5 + 1)))
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
                                            print('colors:        $[red, green, ivory, yellow, blue]                  $')
                                            print('nationalities: $[english, spaniard, ukrainian, japanese, norwegian]$')
                                            print('drinks:        $[coffee, tea, milk, orange, water]                 $')
                                            print('pet:           $[dog, snails, fox, horse, zebra]                   $')
                                            print('cigarettes:    $[gold, kools, west, luckies, camel]                $')
                                            result += {[water, zebra]}
    return result


print(zebraPuzzle())

