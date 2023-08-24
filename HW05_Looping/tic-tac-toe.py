# Author: Eric Gu
# Email: ejgu@umass.edu
# Spire ID: 34231523

import string

def make_empty_board():
    row1 = [" ", " ", " "]
    row2 = [" ", " ", " "]
    row3 = [" ", " ", " "]

    board = [row1, row2, row3]

    return board

def print_board(board):

    print(f" {board[0][0]} | {board[0][1]} | {board[0][2]} ")
    print(f"---+---+---")
    print(f" {board[1][0]} | {board[1][1] } | {board[1][2]} ")
    print(f"---+---+---")
    print(f" {board[2][0]} | {board[2][1] } | {board[2][2]} ")

def get_legal_row_or_col_num():
    
    while True:
        number = int(input("Please enter a row/column number: "))

        if 0 <= number <= 2:
            return number
        else:
            print("Guess was not between 0 and 2.")

def space_empty(board, loc):

    if loc[0] == 0:
        if board[0][loc[1]] == " ":
            return True
    elif loc[0] == 1:
        if board[1][loc[1]] == " ":
            return True
    elif loc[0] == 2:
        if board[2][loc[1]] == " ":
            return True
    
    return False

def get_legal_coordinate(board):

    while True:
        row = get_legal_row_or_col_num()
        column = get_legal_row_or_col_num()
        loc = (row, column)
        if space_empty(board, loc):
            return(loc)
        else:
            print("That space is not empty.")

def update_board(board, loc, player):
    if space_empty(board, loc):
        board[loc[0]][loc[1]] = player

    return board

def has_won(board, player):

    for row in board:
        if all(mark == player for mark in row):
            return True

    for col in range(3):
        if all(row[col] == player for row in board):
            return True

    if (all(board[i][i] == player for i in range(3))) or (all(board[i][2 - i] == player for i in range(3))):
        return True

    return False

def get_winner(board):

    if has_won(board, "X"):
        return 1
    
    if has_won(board, "O"):
        return 2
    
    return 0

def one_turn(board, player):

    p_num = 0

    if player == "X":
        p_num = 1
    else:
        p_num = 2

    print(f"Player {p_num} move:")

    update_board(board, get_legal_coordinate(board), player)
    print_board(board)

    return (board, get_winner(board))

def play_game():

    turns = 0
    board = make_empty_board()

    while turns < 9:
        if turns % 2 == 0:
            one_turn(board, "X")
        else:
            one_turn(board, "O")

        if has_won(board, "X"):
            print("Player 1 Wins!")
            return
        elif has_won(board, "O"):
            print("Player 2 Wins!")
            return
        
        turns += 1
    
    print("Tie!")