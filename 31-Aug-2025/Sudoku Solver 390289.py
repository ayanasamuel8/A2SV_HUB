# Problem: Sudoku Solver - https://leetcode.com/problems/sudoku-solver/description/

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        row_sub = [[0]*10 for _ in range(9)]
        col_sub = [[0]*10 for _ in range(9)]
        box_sub = [[0]*10 for _ in range(9)]

        for r in range(9):
            for c in range(9):
                if board[r][c] != '.':
                    num = int(board[r][c])
                    row_sub[r][num] += 1
                    col_sub[c][num] += 1
                    box_sub[(r//3)*3 + (c//3)][num] += 1

        def valid(r, c, val):
            b = (r//3)*3 + (c//3)
            return row_sub[r][val] == 0 and col_sub[c][val] == 0 and box_sub[b][val] == 0

        def backtrack(r, c):
            if r == 9:
                return True
            if c == 9:
                return backtrack(r+1, 0)
            if board[r][c] != '.':
                return backtrack(r, c+1)

            for num in range(1, 10):
                if valid(r, c, num):
                    board[r][c] = str(num)
                    row_sub[r][num] += 1
                    col_sub[c][num] += 1
                    box_sub[(r//3)*3 + (c//3)][num] += 1

                    if backtrack(r, c+1):
                        return True

                    board[r][c] = '.'
                    row_sub[r][num] -= 1
                    col_sub[c][num] -= 1
                    box_sub[(r//3)*3 + (c//3)][num] -= 1

            return False

        backtrack(0, 0)
