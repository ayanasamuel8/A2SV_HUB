# Problem: Find Eventual Safe States - https://leetcode.com/problems/find-eventual-safe-states/

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        visited = [-1] * (n := len(graph))
        ans = [False] * n
        def dfs(node):
            if not graph[node]:
                ans[node] = True
                visited[node] = 1
                return False
            result = False 
            for v in graph[node]:
                if visited[v] == -1:
                    visited[v] = 0
                    result |= dfs(v)
                elif visited[v] == 0:
                    result = True
                elif not ans[v]:
                    result = True
            if result:
                visited[node] = 1
                return True
            visited[node] = 1
            ans[node] = True
            return False

        for i in range(n):
            if visited[i] == -1:
                visited[i] = 0
                dfs(i)
        
        return [i for i in range(n) if ans[i]]