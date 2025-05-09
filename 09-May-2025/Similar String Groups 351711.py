# Problem: Similar String Groups - https://leetcode.com/problems/similar-string-groups/

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
    def checkAnagram(self, s1, s2):
        if s1 == s2:
            return True
        if Counter(s1) != Counter(s2):
            return False
        n = len(s1)
        diff1 = []
        diff2 = []
        for i in range(n):
            if s1[i] == s2[i]:
                continue
            diff1.append(s1[i])
            diff2.append(s2[i])
        return sorted(diff1) == sorted(diff2) and len(diff1) == 2

    def numSimilarGroups(self, strs: List[str]) -> int:
        n = len(strs)
        dsu = UnionFind(n)
        for i in range(n):
            for j in range(i + 1, n):
                if self.checkAnagram(strs[i], strs[j]):
                    dsu.union(i,j)
        for i in range(n):
            dsu.find(i)
        
        return dsu.size