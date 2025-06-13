# Problem: Minimum Score of a Path Between Two Cities - https://leetcode.com/problems/minimum-score-of-a-path-between-two-cities/description/

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.min_cost = [inf for i in range(n)]
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y, cost):
        xroot = self.find(x)
        yroot = self.find(y)
        if xroot == yroot:
            self.min_cost[yroot] = min(self.min_cost[yroot], cost)
            self.min_cost[xroot] = min(self.min_cost[yroot], cost)
            return
        if self.rank[xroot] < self.rank[yroot]:
            self.parent[xroot] = yroot
            self.min_cost[yroot] = min(self.min_cost[yroot], cost, self.min_cost[xroot])
        else:
            self.parent[yroot] = xroot
            if self.rank[xroot] == self.rank[yroot]:
                self.rank[xroot] += 1
            self.min_cost[xroot] = min(self.min_cost[xroot], cost, self.min_cost[yroot])

class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        dsu = UnionFind(n)
        for u,v, cost in roads:
            u -= 1
            v -= 1
            dsu.union(u,v,cost)
        return dsu.min_cost[dsu.find(0)]
