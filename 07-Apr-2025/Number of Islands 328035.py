# Problem: Number of Islands - https://leetcode.com/problems/number-of-islands/

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n,m = len(grid), len(grid[0])
        visited = [[False] * m for _ in range(n)]
        drxn = [[0,-1],[-1,0],[0,1],[1,0]]

        def valid(newx,newy):
            return 0 <= newx < n and 0 <= newy < m
        
        def dfs(x,y):
            visited[x][y] = True
            for dx,dy in drxn:
                newx = x + dx
                newy = y + dy
                if valid(newx,newy) and not visited[newx][newy] and grid[newx][newy] == '1':
                    dfs(newx,newy)
        
        count = 0

        for row in range(n):
            for col in range(m):
                if grid[row][col] == '1' and not visited[row][col]:
                    count += 1
                    dfs(row, col)
        return count