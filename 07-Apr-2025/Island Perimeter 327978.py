# Problem: Island Perimeter - https://leetcode.com/problems/island-perimeter/description/

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        n,m = len(grid), len(grid[0])

        visited = [[False] * m for _ in range(n)]
        drxn = [[0,-1],[-1,0],[0,1],[1,0]]
        parimeter = 0

        def valid(newx,newy):
            return 0<= newx < n and 0 <= newy < m

        def dfs(x, y):
            nonlocal parimeter
            for dx,dy in drxn:
                newx = x + dx
                newy = y + dy
                if valid(newx,newy):
                    if grid[newx][newy] == 0:
                        parimeter += 1
                    elif not visited[newx][newy]:
                        visited[newx][newy] = True
                        dfs(newx, newy)
                else:
                    parimeter += 1
        for row in range(n):
            for col in range(m):
                if grid[row][col] == 1 and not visited[row][col]:
                    visited[row][col] = True
                    dfs(row, col)
        return parimeter