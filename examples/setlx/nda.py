import setlx


class nda:

    @staticmethod
    @setlx.procedure
    def isEmpty():
        current = setlx.Set([ndaInitial])
        while True:
            inRange = current
            currentPairs = setlx.Set([setlx.List([letter, inState]) for letter in ndaAlphabet for inState in inRange])
            current += setlx.Set([outState for outState in ndaStates if any(setlx.List([letter, inState, outState]) in ndaTransitions for [letter, inState] in currentPairs)])
            if current == inRange:
                break
        if inRange * ndaAccepting != setlx.Set():
            setlx.print('The language accepted by the automaton is not empty')
            return False
        else:
            setlx.print('The language accepted by the automaton is empty')
            return True

    @setlx.procedure
    def __init__(self, alphabet, states, initial, accepting, transitions):
        self.ndaAlphabet = ndaAlphabet = alphabet
        self.ndaStates = ndaStates = states
        self.ndaTransitions = ndaTransitions = transitions
        self.ndaInitial = ndaInitial = initial
        self.ndaAccepting = ndaAccepting = accepting


myNda = nda(setlx.Set(['a', 'b']), setlx.Set([0, 1, 2]), 0, setlx.Set([2]), setlx.Set([setlx.List(['a', 0, 1]), setlx.List(['b', 1, 2])]))
myNda.isEmpty()
myNda = nda(setlx.Set(['a', 'b']), setlx.Set([0, 1, 2]), 0, setlx.Set([2]), setlx.Set([setlx.List(['a', 0, 1]), setlx.List(['b', 0, 1])]))
myNda.isEmpty()

