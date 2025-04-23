# Problem: Find Eventual Safe States - https://leetcode.com/problems/find-eventual-safe-states/

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        visited = [-1] * (n := len(graph))
        ans = set()
        def dfs(node):
            if not graph[node]:
                ans.add(node)
                visited[node] = 1
                return False
            result = False 
            for v in graph[node]:
                if visited[v] == -1:
                    visited[v] = 0
                    result |= dfs(v)
                elif visited[v] == 0:
                    result = True
                elif v not in ans:
                    result = True
            if result:
                visited[node] = 1
                return True
            visited[node] = 1
            ans.add(node)
            return False

        for i in range(n):
            if visited[i] == -1:
                visited[i] = 0
                dfs(i)
        
        return sorted(ans)