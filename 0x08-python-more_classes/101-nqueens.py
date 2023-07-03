#!/usr/bin/python3
import sys


def solve_nqueens(n):
    if not isinstance(n, int):
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    def is_safe(board, row, col):
        for i in range(row):
            if board[i] == col or board[i] - i == col - row or \
                    board[i] + i == col + row:
                return False
        return True

    def backtrack(board, row):
        if row == n:
            solution = [[i, board[i]] for i in range(n)]
            print(solution)
        else:
            for col in range(n):
                if is_safe(board, row, col):
                    board[row] = col
                    backtrack(board, row + 1)

    board = [-1] * n
    backtrack(board, 0)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python 101-nqueens.py N")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
        solve_nqueens(n)
    except ValueError:
        print("N must be a number")
        sys.exit(1)
