# Problem: Unique Paths III - https://leetcode.com/problems/unique-paths-iii/

class Solution:
    
    def backTrack(self, r, c, left, destr, destc, visited, grid):
        
        if r == destr and c == destc:
            self.count += (left == -1)
            return
        for dr, dc in self.dirs_4:
            nr, nc = r + dr, c + dc
            if self.inBound(nr, nc) and visited[nr][nc] != 0 and grid[nr][nc] != -1:
                visited[nr][nc] = 0
                self.backTrack(nr, nc, left - 1, destr, destc, visited, grid)
                visited[nr][nc] = -1
    
    def inBound(self, x, y): 
        return 0 <= x < self.n and 0 <= y < self.m
        
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        left = 0
        self.count = 0
        self.dirs_4 = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        self.n, self.m = len(grid), len(grid[0])
        start = []
        dest = []
        
        for i in range(self.n):
            for j in range(self.m):
                if grid[i][j] == 1:
                    start = [i, j]
                elif grid[i][j] == 2:
                    dest = [i, j]
                elif grid[i][j] == 0:
                    left += 1
        
        visited = [[-1] * self.m for _ in range(self.n)]
        visited[start[0]][start[1]] = 0
        self.backTrack(start[0], start[1], left, dest[0], dest[1], visited, grid)
        
        return self.count