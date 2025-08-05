# Problem: Minimum Obstacle Removal to Reach Corner - https://leetcode.com/problems/minimum-obstacle-removal-to-reach-corner/

class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        # cost, row, col
        q = [(0, 0, 0)]
        n, m = len(grid), len(grid[0])
        dirs_4 = [[0, -1], [-1, 0], [1, 0], [0, 1]]
        grid[0][0] = -1

        def inBound(nrow , ncol):
            return 0 <= nrow < n and 0 <= ncol < m

        while q:
            cost, row, col = heappop(q)
            if row == n - 1 and col == m - 1:
                return cost
            for drow, dcol in dirs_4:
                nrow = row + drow
                ncol = col + dcol
                if inBound(nrow, ncol) and grid[nrow][ncol] != -1:
                    heappush(q, (cost + grid[nrow][ncol], nrow, ncol))
                    grid[nrow][ncol] = -1