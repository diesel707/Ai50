"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    if board == initial_state():
        return X

    if sum([row.count(X) for row in board]) <= sum([row.count(O) for row in board]):
        return X
    else:
        return O

    # raise NotImplementedError


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """

    possible_actions = set()


    for i, row in enumerate(board):
        for j, cell in enumerate(row):
            if cell is None:
                possible_actions.add((i,j))
    return possible_actions

    # raise NotImplementedError


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    m, n = action
    boardcopy = copy.deepcopy(board)
    try:
        if boardcopy[m][n] != EMPTY:
            raise IndexError
    
        boardcopy[m][n] = player(board)
        return boardcopy
    except IndexError:
        print('Use another spot')
    
    # raise NotImplementedError


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for r in board:
        if r[0] is not EMPTY and r[0] == r[1] == r[2]:
            return r[0]

    for c in range(len(board)):
        if board[0][c] is not EMPTY and board[0][c] == board[1][c] == board[2][c]:
            return board[0][c]

    if board[0][0] is not EMPTY and board[0][0] == board[1][1] == board[2][2]:
        return board[0][0]
    
    if board[0][2] is not EMPTY and board[0][2] == board[2][0] == board[1][1]:
        return board[0][2]

    return None
    # raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None or actions(board) == set():
        return True
    return False

    # raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0

    # raise NotImplementedError

def min_value(board):
    if terminal(board):
        return utility(board)

    v = 1

    for a in actions(board):
        v = min(v, max_value(result(board, a)))
        if v == -1:
            break
    return v

def max_value(board):
    if terminal(board):
        return utility(board)

    v = -1
    for a in actions(board):
        v = max(v, min_value(result(board, a)))
        if v == 1:
            break
    return v

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None

    current_player = player(board)

    if current_player == X:
        v = -1
        bestmove = (-1,-1)
        c = sum(row.count(EMPTY) for row in board)
        if c == 9:
            return bestmove
        for action in actions(board):
            move = min_value(result(board, action))
            if move == 1:
                bestmove = action
                break
            if move > v:
                bestmove = action
        return bestmove
    if current_player == O:
        v = 1
        bestmove = (-1,-1)
        for action in actions(board):
            move = max_value(result(board, action))
            if move == -1:
                bestmove = action
                break
            if move < v:
                bestmove = action
        return bestmove
    # raise NotImplementedError
