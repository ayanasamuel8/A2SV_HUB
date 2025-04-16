# Problem: Map of Highest Peak - https://leetcode.com/problems/map-of-highest-peak/description/

class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        active_cell = deque()
        n, m = len(isWater), len(isWater[0])

        drxn = [[-1, 0], [0, -1], [0, 1], [1, 0]]
        visited = [[False] * m for _ in range(n)]

        def inBound(newx, newy):
            return 0 <= newx < n and 0 <= newy < m

        for i in range(n):
            for j in range(m):
                if isWater[i][j]:
                    active_cell.append((i, j))
                    isWater[i][j] = 0
                    visited[i][j] = True

        while active_cell:
            x, y = active_cell.popleft()
            for dx, dy in drxn:
                newx, newy = x + dx, y + dy
                if inBound(newx, newy) and not visited[newx][newy]:
                    visited[newx][newy] = True
                    isWater[newx][newy] = isWater[x][y] + 1
                    active_cell.append((newx, newy))
        
        return isWater