import numpy as np


def coordinate(board, player):
    print("Player {}'s turn".format(player))
    i = int(input('input i: '))
    j = int(input('input j: '))
    while (i > 3 or i < 1 or j < 1 or j > 3) or board[i - 1][j - 1] != 0:
        print('wrong coordination, input again')
        print("Player {}'s turn".format(player))
        i = int(input('input i: '))
        j = int(input('input j: '))
    board[i - 1][j - 1] = player
    return board


def display_board(board):
    board_list = []
    trans_board = board.flatten()
    for i in range(9):
        if trans_board[i] == 0:
            board_list.append(' ')
        elif trans_board[i] == 1:
            board_list.append('X')
        else:
            board_list.append('O')
    print("""
     {} | {} | {}
    ---+---+---
     {} | {} | {}
    ---+---+---
     {} | {} | {}
    """.format(*board_list))


def row_win(board, player):
    nrow, ncol = board.shape
    win = True
    for i in range(nrow):
        win = True
        for j in range(ncol):
            if board[i, j] != player:
                win = False
                continue
        if win:
            return win
    return win


def col_win(board, player):
    nrow, ncol = board.shape
    win = True
    for j in range(ncol):
        win = True
        for i in range(nrow):
            if board[i, j] != player:
                win = False
                continue
        if win:
            return win
    return win


def diag_win(board, player):
    nrow, ncol = board.shape
    win = True
    for i in range(nrow):
        if board[i][i] != player:
            win = False
            continue

    if win:
        return win

    win = True
    for i in range(nrow):
        if board[i][2 - i] != player:
            win = False
            continue
    return win


def check_win(board):
    winner = 0
    for player in [1, 2]:
        if row_win(board, player) or col_win(board, player) or diag_win(board, player):
            winner = player

    if np.all(board != 0) and winner == 0:
        winner = -1
    return winner


board = np.array([[0, 0, 0],
                  [0, 0, 0],
                  [0, 0, 0]])

winner, counter = 0, 1
display_board(board)
while winner == 0:
    for player in [1, 2]:
        board = coordinate(board, player)
        print("Board after " + str(counter) + " move")
        display_board(board)
        counter += 1
        winner = check_win(board)
        if winner != 0:
            break


if winner in [1, 2]:
    print("Winner is: " + str(winner))
else:
    print('Draw')


