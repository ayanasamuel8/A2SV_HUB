# Problem: Largest Color Value in a Directed Graph - https://leetcode.com/problems/largest-color-value-in-a-directed-graph/

class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        n = len(colors)
        indeg = [0] * n
        indeg2 = [0] * n
        for u,v in edges:
            graph[u].append(v)
            indeg[v] += 1
            indeg2[v] += 1
            
        sorted_graph = []
        q = deque()
        for i in range(n):
            if indeg[i] == 0:
                q.append(i)
        while q:
            u = q.popleft()
            sorted_graph.append(u)
            for v in graph[u]:
                indeg[v] -= 1
                if indeg[v] == 0:
                    q.append(v)
        
        if len(sorted_graph) < n:
            return -1
        dp = [[1 if colors[j] == chr(97 + i) else 0 for i in range(26)] for j in range(n)]
        
        q = deque()
        for i in range(n):
            if indeg2[i] == 0:
                q.append(i)
        while q:
            u = q.popleft()
        
            for v in graph[u]:
                indeg2[v] -= 1
                for i in range(26):
                    dp[v][i] = max(dp[v][i], dp[u][i] + (1 if colors[v] == chr(97 + i) else 0))
                if indeg2[v] == 0:
                    q.append(v)
        _max = 1
        for i in range(n):
            for j in range(26):
                _max = max(_max, dp[i][j])
        return _max