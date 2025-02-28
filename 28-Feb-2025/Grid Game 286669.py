# Problem: Grid Game - https://leetcode.com/problems/grid-game/

class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        m =len(grid[0])
        if m <= 1: return 0
        for j in range(m - 2, -1 , -1):
            grid[0][j] += grid[0][j + 1]
            grid[1][m - j - 1] += grid[1][m -  j - 2]
        ans = 0
        for j in range(m - 1):
            if grid[1][j] > grid[0][j + 1]:
                if j > 0: ans = max(grid[0][j + 1], grid[1][j - 1])
                else: ans = grid[0][j + 1]
                break
        else:
            ans = grid[1][m - 2]
        return ans