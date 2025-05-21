# Problem: Regions Cut By Slashes - https://leetcode.com/problems/regions-cut-by-slashes/description/

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.size = n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        xroot = self.find(x)
        yroot = self.find(y)
        if xroot == yroot:
            return
        self.size -= 1
        if self.rank[xroot] < self.rank[yroot]:
            self.parent[xroot] = yroot
        else:
            self.parent[yroot] = xroot
            if self.rank[xroot] == self.rank[yroot]:
                self.rank[xroot] += 1

class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        n = len(grid)
        number_of_classes = n * n * 4
        dsu = UnionFind(number_of_classes)
        for r in range(n):
            for c in range(n):
                index = (r * n) + c
                left = index * 4
                top, right, bottom = left +  1, left + 2, left + 3
                if grid[r][c] == ' ':
                    dsu.union(left, top)
                    dsu.union(left, bottom)
                    dsu.union(right, left)
                elif grid[r][c] == '/':
                    dsu.union(left, top)
                    dsu.union(right, bottom)
                elif grid[r][c] == '\\':
                    dsu.union(top, right)
                    dsu.union(left, bottom)
                if r < n - 1:
                    _next = ((r + 1) * n) + c
                    ntop = (_next * 4 + 1)
                    dsu.union(bottom, ntop)
                if c < n - 1:
                    _next = (r * n) + c + 1
                    nleft = _next * 4
                    dsu.union(nleft, right)
        return dsu.size