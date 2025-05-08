# Problem: Check if There is a Valid Path in a Grid - https://leetcode.com/problems/check-if-there-is-a-valid-path-in-a-grid/

class UnionFind:
    def __init__(self, size):
        self.parent = [i for i in range(size)]
        self.rank = [0] * size
    def find(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x
    def union(self, x, y):
        r_x = self.find(x)
        r_y = self.find(y)
        if r_x == r_y:
            return
        if self.rank[r_x] > self.rank[r_y]:
            self.parent[r_y] = r_x
        elif self.rank[r_y] > self.rank[r_x]:
            self.parent[r_x] = r_y
        else:
            self.parent[r_y] = r_x
            self.rank[r_x] += 1
class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        n, m = len(grid), len(grid[0])
        path = {1:[[0,-1], [0, 1]], 2:[[-1, 0], [1, 0]], 3:[[0, -1], [1, 0]], 4:[[0, 1], [1, 0]], 5:[[0, -1], [-1, 0]], 6:[[0, 1], [-1, 0]]}

        index_map = {}
        start = 0
        for i in range(n):
            for j in range(m):
                index_map[(i, j)] = start
                start += 1

        def inBound(nrow, ncol):
            return 0 <= nrow < n and 0 <= ncol < m
        
        dsu = UnionFind(n * m)
        for i in range(n):
            for j in range(m):
                curr_idx = index_map[(i, j)]
                for di, dj in path[grid[i][j]]:
                    ni, nj = i + di, j + dj
                    if inBound(ni, nj):
                        flag = False
                        for dr, dc in path[grid[ni][nj]]:
                            if ni + dr == i and  nj + dc == j:
                                flag = True
                                break
                        if flag:
                            dsu.union(curr_idx, index_map[(ni, nj)])
        
        return dsu.find(index_map[(0,0)]) == dsu.find(index_map[(n - 1, m - 1)])