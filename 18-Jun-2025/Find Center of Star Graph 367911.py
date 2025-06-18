# Problem: Find Center of Star Graph - https://leetcode.com/problems/find-center-of-star-graph/

class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        n = len(edges) + 1
        graph = [set() for i in range(n)]
        for u,v in edges:
            u -= 1
            v -= 1
            graph[u].add(v)
            graph[v].add(u)
        
        q = deque()
        for i, adj in enumerate(graph):
            if len(adj) == 1:
                q.append(i)
        last = q[0]
        while q:
            for _ in range(len(q)):
                u = q.popleft()
                last = u
                for v in graph[u]:
                    graph[v].remove(u)
                    if len(graph[v]) <= 1:
                        q.append(v)
        return last + 1