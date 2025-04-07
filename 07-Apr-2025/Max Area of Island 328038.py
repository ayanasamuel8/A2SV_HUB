# Problem: Max Area of Island - https://leetcode.com/problems/max-area-of-island/

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        n,m = len(grid), len(grid[0])
        visited = [[False] * m for _ in range(n)]
        drxn = [[0,-1],[-1,0],[0,1],[1,0]]

        def valid(newx,newy):
            return 0 <= newx < n and 0 <= newy <  m

        def dfs(x,y):
            visited[x][y] = True
            count = 1
            
            for dx,dy in drxn:
                newx = x + dx
                newy = y + dy

                if valid(newx, newy) and not visited[newx][newy] and grid[newx][newy] == 1:
                    count += dfs(newx,newy)
            
            return count
        
        max_count = 0

        for row in range(n):
            for col in range(m):
                if not visited[row][col] and grid[row][col] == 1:
                    max_count = max(max_count, dfs(row, col))
                    print(max_count)
        
        return max_count