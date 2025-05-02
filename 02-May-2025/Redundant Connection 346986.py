# Problem: Redundant Connection - https://leetcode.com/problems/redundant-connection/

class UnionFind:
    def __init__(self, size):
        self.parent = [i for i in range(size)]
        self.rank = [0] * size
        
    def find(self, x):
        if self.parent[x] == x:
            return x
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
                
        
    def union(self, x, y):
        r_x = self.find(x)
        r_y = self.find(y)
        if r_x == r_y: return
        if self.rank[r_y] < self.rank[r_x]:
            self.parent[r_y] = r_x
        elif self.rank[r_y] > self.rank[r_x]:
            self.parent[r_x] = r_y
        else:
            self.parent[r_x] = r_y
            self.rank[r_y] += 1
                
    def connected(self, x, y):
        return self.find(x) == self.find(y)
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        dsu = UnionFind(n)
        for u,v in edges:
            u -= 1
            v -= 1
            if dsu.connected(u,v):
                return [u + 1, v + 1]
            dsu.union(u , v)