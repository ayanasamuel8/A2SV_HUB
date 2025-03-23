# Problem: Number of Ways to Arrive at Destination - https://leetcode.com/problems/number-of-ways-to-arrive-at-destination/

class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        path = [0] * n
        path[0] = 1
        adj = defaultdict(list)
        costs = [inf] * n
        costs[0] = 0
        MOD = int(1e9 + 7)

        for u,v,time in roads:
            adj[u].append((v,time))
            adj[v].append((u,time))
        
        min_heap = [(0,0)]
        heapify(min_heap)
        visited = [False] * n

        while min_heap:
            [cost, u] = heappop(min_heap)
            for v, time in adj[u]:
                new_cost = cost + time
                if new_cost < costs[v]:
                    costs[v] = new_cost
                    path[v] = path[u]
                    heappush(min_heap, (new_cost, v))
                elif new_cost == costs[v]:
                    path[v] = (path[v] + path[u]) % MOD
        return path[n - 1] % MOD

        
            