# Problem: Count the Number of Complete Components - https://leetcode.com/problems/count-the-number-of-complete-components/

class Solution:
    def isComplete(self, curr, adj, seen):
        queue = deque([curr])
        visited = set([curr])
        seen[curr] = True

        while queue:
            u = queue.popleft()
            for v in adj[u]:
                if v not in visited:
                    seen[v] = True
                    visited.add(v)
                    queue.append(v)
        
        edges = 0
        for v in visited:
            edges += len(adj[v])
            
        return (edges//2) == (len(visited) * (len(visited) - 1)//2)


    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:

        adj = defaultdict(list)
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visited = [False] * n
        count = 0

        for i in range(n):
            if not visited[i] and self.isComplete(i, adj,visited):
                count += 1

        return count

