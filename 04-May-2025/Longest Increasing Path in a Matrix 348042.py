# Problem: Longest Increasing Path in a Matrix - https://leetcode.com/problems/longest-increasing-path-in-a-matrix/

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        n, m = len(matrix), len(matrix[0])
        indeg = [[0] * m for _ in range(n)]
        distance = [[0] * m for _ in range(n)]
       
        def inBound(x, y): 
            return 0 <= x < n and 0 <= y < m
        dirs_4 = [(-1, 0), (0, -1), (1, 0), (0, 1)]

        def indegCount(row, col):
            for dr, dc in dirs_4:
                nrow, ncol = row + dr, col + dc
                if inBound(nrow, ncol) and matrix[nrow][ncol] < matrix[row][col]:
                    indeg[row][col] += 1
          

        q = deque()
        for i in range(n):
            for j in range(m):
                indegCount(i, j)
                if indeg[i][j] == 0:
                    q.append((i, j))
                    distance[i][j] = 1
        
        ans = 1
        while q:
            row, col = q.popleft()
            ans = max(ans, distance[row][col])
            for dr, dc in dirs_4:
                nrow, ncol = row + dr, col + dc
                if inBound(nrow, ncol) and matrix[nrow][ncol] > matrix[row][col]:
                    indeg[nrow][ncol] -= 1
                    distance[nrow][ncol] = max(distance[nrow][ncol], distance[row][col] + 1)
                    if indeg[nrow][ncol] == 0:
                        q.append((nrow, ncol))
        return ans