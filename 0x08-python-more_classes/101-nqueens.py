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
            if board[i][col] == 'Q':
                return False
        
        i = row - 1
        j = col - 1
        while i >= 0 and j >= 0:
            if board[i][j] == 'Q':
                return False
            i -= 1
            j -= 1
        

        i = row - 1
        j = col + 1
        while i >= 0 and j < n:
            if board[i][j] == 'Q':
                return False
            i -= 1
            j += 1
        
        return True

    def backtrack(board, row):
        if row == n:
            for i in range(n):
                print(''.join(board[i]))
            print()
        else:
            for col in range(n):
                if is_safe(board, row, col):
                    board[row][col] = 'Q'
                    backtrack(board, row + 1)
                    board[row][col] = '.'

    board = [['.' for _ in range(n)] for _ in range(n)]
    backtrack(board, 0)

    if __name__ == '__main__':
        if len(sys.argv) != 2:
            print("Usage: nqueens N")
            sys.exit(1)
        try:
            n = int(sys.argv[1])
            solve_nqueens(n)
        except ValueError:
            print("N must be a number")
        sys.exit(1)
