# Problem: Is Graph Bipartite? - https://leetcode.com/problems/is-graph-bipartite/

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        color = [-1] * len(graph)

        def dfs(node):
            for nbr in graph[node]:
                if color[nbr] != -1:
                    if color[nbr] == color[node]:
                        return False
                else:
                    color[nbr] = not color[node]
                    if not dfs(nbr):
                        return False
            return True
        
        for i in range(len(graph)):
            if color[i] == -1:
                color[i] = True
                if not dfs(i):
                    return False
        return True
        