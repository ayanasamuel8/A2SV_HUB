# Problem: Find if Path Exists in Graph - https://leetcode.com/problems/find-if-path-exists-in-graph/

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        adj = [[] for _ in range(n)]
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        visited = [False] * n
        
        def dfs(node):
            if node == destination:
                return True
            for nbr in adj[node]:
                if not visited[nbr]:
                    visited[nbr] = True
                    if dfs(nbr):
                        return True
            return False
        return dfs(source)