# Problem: Most Stones Removed with Same Row or Column - https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        xroot = self.find(x)
        yroot = self.find(y)
        if xroot == yroot:
            return
        if self.rank[xroot] < self.rank[yroot]:
            self.parent[xroot] = yroot
        else:
            self.parent[yroot] = xroot
            if self.rank[xroot] == self.rank[yroot]:
                self.rank[xroot] += 1

class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        n = len(stones)
        row_index = defaultdict(list)
        col_index = defaultdict(list)
        dsu = UnionFind(n)
        for i, (row, col) in enumerate(stones):
            row_index[row].append(i)
            col_index[col].append(i)
        for val in row_index.values():
            size = len(val)
            for i in range(1, size):
                dsu.union(val[i], val[i - 1])
        for val in col_index.values():
            size = len(val)
            for i in range(1, size):
                dsu.union(val[i], val[i - 1])
        for i in range(n):
            dsu.find(i)
        
        st = set(dsu.parent)
        return n - len(st)