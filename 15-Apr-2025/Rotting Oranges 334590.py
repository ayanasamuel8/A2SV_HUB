# Problem: Rotting Oranges - https://leetcode.com/problems/rotting-oranges/

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        rottenOranges = deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    rottenOranges.append((i,j))
        
        def inbound(newx, newy):
            return 0 <= newx < m and 0 <= newy < n
        
        minutesElapse = 0
        drxn = [[-1, 0], [0, -1], [0, 1], [1, 0]]
        while rottenOranges:
            size = len(rottenOranges)
            for i in range(size):
                x, y = rottenOranges.popleft()
                for dx, dy in drxn:
                    newx, newy = x + dx, y + dy
                    if inbound(newx, newy) and grid[newx][newy] == 1:
                        grid[newx][newy] = 2
                        rottenOranges.append((newx, newy))
            minutesElapse += 1
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    return -1
        return minutesElapse - 1 if minutesElapse > 0 else 0