# Problem: Possible Bipartition - https://leetcode.com/problems/possible-bipartition/

class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        color = [-1] * (n + 1)
        adj = [[] for _ in range(n + 1)]
        for a,b in dislikes:
            adj[a].append(b)
            adj[b].append(a)

        def dfs(node):
            for nbr in adj[node]:
                if color[nbr] != -1:
                    if color[nbr] == color[node]:
                        return False
                else:
                    color[nbr] = not color[node]
                    if not dfs(nbr):
                        return False
            return True
        for i in range(1,n + 1):
            if color[i] == -1:
                color[i] = True
                if not dfs(i):
                    return False
        return True