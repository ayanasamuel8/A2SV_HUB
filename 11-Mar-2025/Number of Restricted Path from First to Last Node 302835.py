# Problem: Number of Restricted Path from First to Last Node - https://leetcode.com/problems/number-of-restricted-paths-from-first-to-last-node/

class Solution:
    def countRestrictedPaths(self, n: int, edges: List[List[int]]) -> int:
        cost_node = defaultdict(lambda:float('inf'))
        cost_node[n] = 0
        adj = defaultdict(list)
        for u,v,cost in edges:
            adj[u].append((v,cost))
            adj[v].append((u,cost))
        # visited = [False] * n
        pq = [(0,n)]
        heapify(pq)
        visited = [False] * (n + 1)
        while pq:
            cost, u = heappop(pq)
            if visited[u]:
                continue
            visited[u] = True
            for nbr, edge_cost in adj[u]:
                if not visited[nbr]:
                    new_cost = cost_node[u] + edge_cost
                    if new_cost < cost_node[nbr]:
                        cost_node[nbr] = new_cost
                        heappush(pq, (new_cost, nbr))
        count = [0] * n
        visited = [False] * n
        count[n - 1] = 1
        visited[n - 1] = True
        def dfs(curr):
            for nbr, cost in adj[curr]:
                if cost_node[nbr] < cost_node[curr]:
                    if visited[nbr - 1]: 
                        count[curr - 1] += count[nbr - 1]
                    else:
                        visited[nbr - 1] = True
                        count[curr - 1] += dfs(nbr)
            return count[curr - 1]

        return dfs(1) % (int(1e9 + 7))
