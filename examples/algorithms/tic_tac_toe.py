import setlx


class tic_tac_toe:

    @setlx.procedure
    def __init__(self, size):
        self.mSize = mSize = setlx.copy(size)
        self.mBoard = mBoard = setlx.List([setlx.List([' ' for col in setlx.List(setlx._range(1, mSize))]) for row in setlx.List(setlx._range(1, mSize))])

        @setlx.procedure
        def square(row, col):
            return mBoard[row][col]
        self.square = square

        @setlx.procedure
        def empty_squares():
            rng = setlx.List(setlx._range(1, mSize))
            return setlx.List([setlx.List([row, col]) for row in rng for col in rng if mBoard[row][col] == ' '])
        self.empty_squares = empty_squares

        @setlx.procedure
        def move(row, col, mark):
            mBoard[row][col] = mark
        self.move = move

        @setlx.procedure
        def f_str():
            rng = setlx.List(setlx._range(1, mSize))
            ls = '\\n' + '-' * (4 * mSize + 1) + '\\n'
            return ls + setlx.join(setlx.List([('| ' + setlx.join(setlx.List([mBoard[row][col] for col in rng]), ' | ') + ' |') for row in rng]), ls) + ls
        self.f_str = f_str

        @setlx.procedure
        def clone():
            result = tic_tac_toe(mSize)
            result.mBoard = mBoard
            return result
        self.clone = clone

        @setlx.procedure
        def check_win():
            rng = setlx.List(setlx._range(1, mSize))
            lines = setlx.List([setlx.List([mBoard[row][col] for col in rng]) for row in rng])
            lines += setlx.List([setlx.List([mBoard[row][col] for row in rng]) for col in rng])
            lines += setlx.List([setlx.List([mBoard[idx][idx] for idx in rng])])
            lines += setlx.List([setlx.List([mBoard[idx][mSize - (idx - 1)] for idx in rng])])
            for line in lines:
                if len(setlx.Set([p for p in line])) == 1 and line[1] != ' ':
                    return line[1]
            if len(self.empty_squares()) == 0:
                return ' '
        self.check_win = check_win


@setlx.procedure
def switch_player(player):
    if player == 'X':
        return 'O'
    elif player == 'O':
        return 'X'
    else:
        setlx.throw(f'illegal argument in switch_player({player})')


@setlx.procedure
def play_game(move_function, user, size):
    board = tic_tac_toe(size)
    player = 'X'
    setlx.print(board)
    while not winner in setlx.Set(['X', 'O', ' ']):
        if user == player:
            [row, col] = setlx.split(setlx.read('enter move as row, col: '), ' *, *')
            [row, col] = setlx.List([setlx.int(row), setlx.int(col)])
        else:
            [row, col] = move_function(board, switch_player(user))
            setlx.print(f'\\ncomputers move: ({row}, {col})')
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


@setlx.procedure
def ttt_quality(board, move, player):
    [row, col] = move
    copy = board.clone()
    copy.move(row, col, player)
    return -ttt_utility(copy, switch_player(player))


@setlx.cached_procedure
def ttt_utility(board, player):
    winner = board.check_win()
    if winner in setlx.Set(['X', 'O', ' ']):
        if winner == player:
            return 1
        elif winner == ' ':
            return 0
        else:
            return -1
    return setlx.max(setlx.Set([ttt_quality(board, move, player) for move in board.empty_squares()]))


@setlx.procedure
def optimal_strategy(board, player):
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


@setlx.procedure
def random_strategy(board, player):
    return setlx.rnd(board.empty_squares())


play_game(optimal_strategy, 'X', 3)

