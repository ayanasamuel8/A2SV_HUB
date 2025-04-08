# Problem: Surrounded Regions - https://leetcode.com/problems/surrounded-regions/

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        n,m = len(board), len(board[0])
        def inbound(newx,newy):
            return 0<= newx < n and 0 <= newy < m
        
        drxn = [[0,-1],[-1,0],[0,1],[1,0]]
        
        def dfs(row, col):
            for dx, dy in drxn:
                newrow = row + dx
                newcol = col + dy
                if inbound(newrow, newcol) and board[newrow][newcol] == 'O':
                    board[newrow][newcol] = 'L'
                    dfs(newrow, newcol)
        #for the top row
        for i in range(m):
            if board[0][i] == 'O':
                board[0][i] = 'L'
                dfs(0, i)
        #for bottom row
        for i in range(m):
            if board[n - 1][i] == 'O':
                board[n - 1][i] = 'L'
                dfs(n - 1, i)
        #for the left col
        for i in range(n):
            if board[i][0] == 'O':
                board[i][0] = 'L'
                dfs(i, 0)
        #for the right col
        for i in range(n):
            if board[i][m - 1] == 'O':
                board[i][m - 1] = 'L'
                dfs(i, m - 1)
        
        for i in range(n):
            for j in range(m):
                if board[i][j] == 'L':
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'