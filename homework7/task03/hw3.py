"""
Given a Tic-Tac-Toe 3x3 board (can be unfinished).
Write a function that checks if the are some winners.
If there is "x" winner, function should return "x wins!"
If there is "o" winner, function should return "o wins!"
If there is a draw, function should return "draw!"
If board is unfinished, function should return "unfinished!"

Example:
    [[-, -, o],
     [-, x, o],
     [x, o, x]]
    Return value should be "unfinished"

    [[-, -, o],
     [-, o, o],
     [x, x, x]]

     Return value should be "x wins!"

"""
from typing import List


#   absolutely ugly code, but it's work
def tic_tac_toe_checker(board: List[List]) -> str:
    flag = False
    for row in board:
        if row[0] == row[1] == row[2] == "-":
            pass
        else:
            flag = True
    if not flag:
        return "unfinished!"
    for row in board:
        if row[0] == row[1] == row[2]:
            return str(row[0]) + " wins!"
    for k in range(3):
        cache = []
        for j in range(3):
            cache.append(board[j][k])
        if cache[0] == cache[1] == cache[2]:
            return str(cache[0]) + " wins!"
    if board[0][0] == board[1][1] == board[2][2]:
        return str(board[1][1]) + " wins!"
    if board[2][0] == board[1][1] == board[0][2]:
        return str(board[1][1]) + " wins!"
    flag2 = False
    for k in range(3):
        for j in range(3):
            if board[k][j] == "-":
                flag2 = True
    if flag2:
        return "unfinished!"
    else:
        return "draw!"
