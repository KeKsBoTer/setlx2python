from setlx.native import *
import setlx


class nda:

    @staticmethod
    @setlx.procedure
    def isEmpty():
        current = {ndaInitial}
        while True:
            inRange = current
            currentPairs = {[letter, inState] for letter in ndaAlphabet for inState in inRange}
            current += {outState for outState in ndaStates if any([([letter, inState, outState] in ndaTransitions) for [letter, inState] in currentPairs])}
            if current == inRange:
                break
        if inRange * ndaAccepting != set():
            print('The language accepted by the automaton is not empty')
            return False
        else:
            print('The language accepted by the automaton is empty')
            return True

    @setlx.procedure
    def __init__(self, alphabet, states, initial, accepting, transitions):
        self.ndaAlphabet = ndaAlphabet = alphabet
        self.ndaStates = ndaStates = states
        self.ndaTransitions = ndaTransitions = transitions
        self.ndaInitial = ndaInitial = initial
        self.ndaAccepting = ndaAccepting = accepting


myNda = nda({'a', 'b'}, {0, 1, 2}, 0, {2}, {['a', 0, 1], ['b', 1, 2]})
myNda.isEmpty()
myNda = nda({'a', 'b'}, {0, 1, 2}, 0, {2}, {['a', 0, 1], ['b', 0, 1]})
myNda.isEmpty()

