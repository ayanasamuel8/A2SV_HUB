# Problem: 01 Matrix - https://leetcode.com/problems/01-matrix/

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        n,m = len(mat), len(mat[0])
        
        result = [[inf] * m for _ in range(n)]
        active_cell = deque()
        drxn = [[-1, 0], [0, -1], [0, 1], [1, 0]]

        def inBound(newx, newy):
            return 0 <= newx < n and 0 <= newy < m

        for i in range(n):
            for j in range(m):
                if not mat[i][j]:
                    result[i][j] = 0
                    active_cell.append((i,j))
        
        while active_cell:
            x, y = active_cell.popleft()

            for dx, dy in drxn:
                newx, newy = x + dx, y + dy
                if inBound(newx, newy) and result[x][y] + 1 < result[newx][newy]:
                    result[newx][newy] = result[x][y] + 1
                    active_cell.append((newx, newy))
        
        return result