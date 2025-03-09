# Problem: Game of Life - https://leetcode.com/problems/game-of-life/description/

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        n,m = len(board), len(board[0])
        """
        Do not return anything, modify board in-place instead.
        """
        def is_valid(x, y):
            nonlocal n,m
            return x >= 0 and y >= 0 and x<n and y<m
        drxn = [[-1,0],[0,-1],[-1,-1],[1,-1], [-1,1],[0,1], [1,0],[1,1]]
        for i in range(n):
            for j in range(m):
                live = 0
                for dx, dy in drxn:
                    x = i + dx
                    y = j + dy
                    if is_valid(x,y):
                        live += board[x][y] == 1 or board[x][y] == '0'
                if live < 2 and board[i][j] == 1:
                    board[i][j] = '0'
                elif live > 3 and board[i][j] == 1:
                    board[i][j] = '0'
                elif live == 3 and board[i][j] == 0:
                    board[i][j] = '1'
        board[:] = [[int(c) for c in row] for row in board]