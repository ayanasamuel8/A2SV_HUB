# Problem: Accounts Merge - https://leetcode.com/problems/accounts-merge/

class UnionFind:
    def __init__(self, n):
        self.parent = dict()
        self.rank = defaultdict(int)

    def find(self, x):
        if x not in self.parent:
            self.parent[x] = x
            return x
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
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        indexed_email = {}
        n = len(accounts)
        for i in range(n):
            name = accounts[i][0]
            for email in accounts[i][1:]:
                indexed_email[email] = name
        dsu = UnionFind(len(indexed_email))
        for i in range(n):
            for j in range(2, len(accounts[i])):
                dsu.union(accounts[i][j], accounts[i][j - 1])
        
        result_dict = defaultdict(set)  
        for i in range(n):
            for email in accounts[i][1:]:
                rep = dsu.find(email)
                result_dict[rep].add(email)
        ans = []
        for key, val in result_dict.items():
            ans.append([indexed_email[key], *sorted(val)])
        return ans