# Problem: Longest Cycle in a Graph - https://leetcode.com/problems/longest-cycle-in-a-graph/

class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        indeg = [0] * (n:= len(edges))
        for i in edges:
            if i != -1:
                indeg[i] += 1
        
        zeroIndeg = deque()
        for i in range(n):
            if indeg[i] == 0:
                zeroIndeg.append(i)
        visited = [False] * n
        while zeroIndeg:
            zero = zeroIndeg.popleft()
            visited[zero] = True
            if edges[zero] != -1:
                indeg[edges[zero]] -= 1
                if indeg[edges[zero]] == 0:
                    zeroIndeg.append(edges[zero])
        
        def dfs(node):
            visited[node] = True
            cnt = 1
            if not visited[edges[node]] and edges[node] != -1:
                cnt += dfs(edges[node])
            return cnt

        ans = -1
        for i in range(n):
            if not visited[i]:
                ans = max(ans, dfs(i))
        
        return ans