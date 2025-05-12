# Problem: Remove Max Number of Edges to Keep Graph Fully Traversable - https://leetcode.com/problems/remove-max-number-of-edges-to-keep-graph-fully-traversable/

class UnionFind:
    def __init__(self, n):
        self.bob = list(range(n))
        self.alice = list(range(n))
        self.ranka = [0] * n
        self.rankb = [0] * n
        self.sizea = n
        self.sizeb = n

    def findBob(self, x):
        if self.bob[x] != x:
            self.bob[x] = self.findBob(self.bob[x])
        return self.bob[x]
    def findAlice(self, x):
        if self.alice[x] != x:
            self.alice[x] = self.findAlice(self.alice[x])
        return self.alice[x]

    def unionBob(self, x, y):
        xroot = self.findBob(x)
        yroot = self.findBob(y)
        if xroot == yroot:
            return True
        self.sizeb -= 1
        if self.rankb[xroot] < self.rankb[yroot]:
            self.bob[xroot] = yroot
        else:
            self.bob[yroot] = xroot
            if self.rankb[xroot] == self.rankb[yroot]:
                self.rankb[xroot] += 1
        return False
    
    def unionAlice(self, x, y):
        xroot = self.findAlice(x)
        yroot = self.findAlice(y)
        if xroot == yroot:
            return True
        self.sizea -= 1
        if self.ranka[xroot] < self.ranka[yroot]:
            self.alice[xroot] = yroot
        else:
            self.alice[yroot] = xroot
            if self.ranka[xroot] == self.ranka[yroot]:
                self.ranka[xroot] += 1
        return False
    
    def unionBoth(self, x, y):
        alice =  self.unionAlice(x, y)
        bob = self.unionBob(x, y)
        return alice and bob

class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        edges.sort(reverse = True)
        dsu = UnionFind(n)
        additional = 0
        for typei, u, v in edges:
            if typei == 1:
                additional += int(dsu.unionAlice(u - 1, v - 1))
            elif typei == 2:
                additional += int(dsu.unionBob(u - 1, v - 1))
            else:
                additional += int(dsu.unionBoth(u - 1, v - 1))
        for i in range(n):
            dsu.findBob(i)
            dsu.findAlice(i)
        return additional if dsu.sizea == dsu.sizeb == 1 else -1