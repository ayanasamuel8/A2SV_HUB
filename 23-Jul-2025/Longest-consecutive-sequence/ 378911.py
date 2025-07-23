# Problem: Longest-consecutive-sequence/ - https://leetcode.com/problems/longest-consecutive-sequence/

class UnionFind:
    def __init__(self):
        self.parent = {}
        self.rank = defaultdict(int)
    
    def find(self, x):
        if x not in self.parent:
            self.parent[x] = x
            return x
        if self.parent[x] != x:
            self.parent[x] =  self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        xroot = self.find(x)
        yroot = self.find(y)
        
        if xroot != yroot:
            if self.rank[xroot] < self.rank[yroot]:
                self.parent[xroot] = yroot
            else:
                self.parent[yroot] = xroot
                if self.rank[xroot] == self.rank[yroot]:
                    self.rank[xroot] += 1

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0
        n = len(nums)
        dsu = UnionFind()
        for num in nums:
            if num - 1 in dsu.parent:
                dsu.union(num - 1, num)
            if num + 1 in dsu.parent:
                dsu.union(num + 1, num)
            dsu.find(num)
        
        for num in nums:
            dsu.find(num)
        return max(list(Counter(dsu.parent.values()).values()))