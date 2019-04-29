import setlx


class tic_tac_toe(setlx.SetlXClass):

    def __init__(self, size):
        [size] = setlx.copy([size])
        self.mSize = setlx.copy(size)
        self.mBoard = setlx.List([setlx.List([' ' for col in setlx.List(setlx._range(1, self.mSize))]) for row in setlx.List(setlx._range(1, self.mSize))])

        def square(self, row, col):
            [row, col] = setlx.copy([row, col])
            return self.mBoard[row][col]
        self.square = setlx.to_method(self, square)

        def empty_squares(self):
            rng = setlx.List(setlx._range(1, self.mSize))
            return setlx.List([setlx.List([row, col]) for row in rng for col in rng if self.mBoard[row][col] == ' '])
        self.empty_squares = setlx.to_method(self, empty_squares)

        def move(self, row, col, mark):
            [row, col, mark] = setlx.copy([row, col, mark])
            self.mBoard[row][col] = setlx.copy(mark)
        self.move = setlx.to_method(self, move)

        def f_str(self):
            rng = setlx.List(setlx._range(1, self.mSize))
            ls = '\n' + '-' * (4 * self.mSize + 1) + '\n'
            return ls + setlx.join(setlx.List([('| ' + setlx.join(setlx.List([self.mBoard[row][col] for col in rng]), ' | ') + ' |') for row in rng]), ls) + ls
        self.f_str = setlx.to_method(self, f_str)

        def clone(self):
            result = tic_tac_toe(self.mSize)
            result.mBoard = setlx.copy(self.mBoard)
            return result
        self.clone = setlx.to_method(self, clone)

        def check_win(self):
            rng = setlx.List(setlx._range(1, self.mSize))
            lines = setlx.List([setlx.List([self.mBoard[row][col] for col in rng]) for row in rng])
            lines += setlx.List([setlx.List([self.mBoard[row][col] for row in rng]) for col in rng])
            lines += setlx.List([setlx.List([self.mBoard[idx][idx] for idx in rng])])
            lines += setlx.List([setlx.List([self.mBoard[idx][self.mSize - (idx - 1)] for idx in rng])])
            for line in lines:
                if len(setlx.Set([p for p in line])) == 1 and line[1] != ' ':
                    return line[1]
            if len(self.empty_squares()) == 0:
                return ' '
        self.check_win = setlx.to_method(self, check_win)


def switch_player(player):
    [player] = setlx.copy([player])
    if player == 'X':
        return 'O'
    elif player == 'O':
        return 'X'
    else:
        setlx.throw(f'illegal argument in switch_player({player})')


def play_game(move_function, user, size):
    [move_function, user, size] = setlx.copy([move_function, user, size])
    board = tic_tac_toe(size)
    player = 'X'
    setlx.print(board)
    while not winner in setlx.Set(['X', 'O', ' ']):
        if user == player:
            [row, col] = setlx.split(setlx.read('enter move as row, col: '), ' *, *')
            [row, col] = setlx.List([setlx.int(row), setlx.int(col)])
        else:
            [row, col] = move_function(board, switch_player(user))
            setlx.print(f'\ncomputers move: ({row}, {col})')
        board.move(row, col, player)
        winner = board.check_win()
        player = switch_player(player)
        setlx.print(board)
        if winner == 'X':
            setlx.print('X wins!')
        elif winner == 'O':
            setlx.print('O wins!')
        elif winner == ' ':
            setlx.print("It's a tie!")


def ttt_quality(board, move, player):
    [board, move, player] = setlx.copy([board, move, player])
    [row, col] = setlx.copy(move)
    copy = board.clone()
    copy.move(row, col, player)
    return -ttt_utility(copy, switch_player(player))


@setlx.cached_procedure
def ttt_utility(board, player):
    [board, player] = setlx.copy([board, player])
    winner = board.check_win()
    if winner in setlx.Set(['X', 'O', ' ']):
        if winner == player:
            return 1
        elif winner == ' ':
            return 0
        else:
            return -1
    return setlx.max(setlx.Set([ttt_quality(board, move, player) for move in board.empty_squares()]))


def optimal_strategy(board, player):
    [board, player] = setlx.copy([board, player])
    best_value = ttt_utility(board, player)
    optimal_moves = setlx.List()
    for move in board.empty_squares():
        if best_value == ttt_quality(board, move, player):
            optimal_moves += setlx.List([move])
    if optimal_moves == setlx.List():
        setlx.print('Error in optimal_strategy')
        setlx.print(board)
        setlx.print(f'player     = {player}')
        setlx.print(f'best_value = {best_value}')
        setlx.throw('ERROR')
    return setlx.rnd(optimal_moves)


def random_strategy(board, player):
    [board, player] = setlx.copy([board, player])
    return setlx.rnd(board.empty_squares())


play_game(optimal_strategy, 'X', 3)
