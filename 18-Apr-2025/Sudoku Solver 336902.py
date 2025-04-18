# Problem: Sudoku Solver - https://leetcode.com/problems/sudoku-solver/description/

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        vertical, horizontal = defaultdict(set), defaultdict(set)
        for row in range(9):
            for col in range(9):
                if board[row][col] != ".":
                    vertical[row].add(int(board[row][col]))
                    horizontal[col].add(int(board[row][col]))

        def checker(row,col,num):
            nonlocal vertical, horizontal
            if num in vertical[row] or num in horizontal[col]:
                return False
            for r in range(row-(row%3),row-(row%3) + 3):
                for c in range(col-(col%3), col-(col%3) + 3):
                    if board[r][c] != "." and int(board[r][c]) == num: return False
            return True

        def backtrack(row,col):
            nonlocal vertical, horizontal
            stop = False
            while row < 9:
                while col < 9:
                    if board[row][col] == ".":
                        stop = True
                        break
                    col += 1
                if stop: break
                col = 0
                row += 1
            if row >= 9: return True
            for num in range(1,10):
                if checker(row,col,num):
                    vertical[row].add(num)
                    horizontal[col].add(num)
                    board[row][col] = str(num)
                    result = backtrack(row,col)
                    if result: return True
                    board[row][col] = "."
                    vertical[row].remove(num)
                    horizontal[col].remove(num)
            return False
        backtrack(0,0)
        return 