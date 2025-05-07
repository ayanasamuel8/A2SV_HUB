# Problem: Min Cost to Connect All Points - https://leetcode.com/problems/min-cost-to-connect-all-points/

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
            return True
        if self.rank[r_x] > self.rank[r_y]:
            self.parent[r_y] = r_x
        elif self.rank[r_y] > self.rank[r_x]:
            self.parent[r_x] = r_y
        else:
            self.parent[r_y] = r_x
            self.rank[r_x] += 1
        return False
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        edges = []
        n = len(points)
        for i in range(n):
            x1, y1 = points[i]
            for j in range(i + 1,n):
                x2, y2 = points[j]
                distance = abs(x2 - x1) + abs(y2 - y1)
                edges.append((distance, i, j))
        edges.sort()
        dsu = UnionFind(len(points))
        ans = 0
        for w,u,v in edges:
            if not dsu.union(u,v):
                ans += w
        return ans