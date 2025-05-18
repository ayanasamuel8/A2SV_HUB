# Problem: Checking Existence of Edge Length Limited Paths - https://leetcode.com/problems/checking-existence-of-edge-length-limited-paths/

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
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        dsu = UnionFind(n)
        edgeList.sort(key=lambda x: x[2])
        queries = [(val, idx) for idx, val in enumerate(queries)]
        queries.sort(key=lambda x: x[0][2])
        ans = [False] * len(queries)
        idx = 0
        for (u,v,limit), i in queries:
            while idx < len(edgeList) and limit > edgeList[idx][2]:
                dsu.union(edgeList[idx][0],edgeList[idx][1])
                idx += 1
            ans[i] = (dsu.find(u) == dsu.find(v))
        return ans
