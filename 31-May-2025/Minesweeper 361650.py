# Problem: Minesweeper - https://leetcode.com/problems/minesweeper/

class Solution:
    def hasMine(self, board, row, col):
        count = 0
        for drow, dcol in self.dirs_8:
            nrow, ncol = row + drow, col + dcol
            if self.inBound(nrow, ncol) and board[nrow][ncol] == 'M':
                count += 1
        return count

    def inBound(self, row, col):
        return 0 <= row < self.n and 0 <= col < self.m
    
    def reveal(self, row, col, board):
        mines = self.hasMine(board, row, col)
        if mines > 0:
            board[row][col] = str(mines)
            return
        board[row][col] = 'B'
        for drow, dcol in self.dirs_8:
            nrow, ncol = row + drow, col + dcol
            if self.inBound(nrow, ncol) and board[nrow][ncol] == 'E':
                self.reveal(nrow, ncol, board)

    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        self.n = len(board)
        self.m = len(board[0])
        self.dirs_8 = [[-1, 0], [0, -1], [-1, -1], [-1, 1], [1, -1], [1, 0], [0, 1], [1, 1]]
        x, y = click[0], click[1]
        if board[x][y] == 'M':
            board[x][y] = 'X'
            return board
        self.reveal(x, y, board)
        return board
