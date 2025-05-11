# Problem: Lexicographically Smallest Equivalent String - https://leetcode.com/problems/lexicographically-smallest-equivalent-string/

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
            return 

        if self.rank[r_x] > self.rank[r_y]:
            self.parent[r_y] = r_x
        elif self.rank[r_y] > self.rank[r_x]:
            self.parent[r_x] = r_y
        else:
            self.parent[r_y] = r_x
            self.rank[r_x] += 1
        
class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        n, m = len(s1), len(baseStr)

        #forming relation
        dsu = UnionFind(26)
        for i in range(n):
            dsu.union(ord(s1[i]) - 97, ord(s2[i]) - 97)
        
        #finding lexicographically smallest equivalent string to baseStr
        ans = []
        for i in range(m):
            curr_char = ord(baseStr[i]) - 97
            for i in range(26):
                if dsu.find(curr_char) == dsu.find(i):
                    ans.append(chr(97 + i))
                    break
        return ''.join(ans)