# Problem: Network Delay Time - https://leetcode.com/problems/network-delay-time/

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for u,v,cost in times:
            u -= 1
            v -= 1
            graph[u].append((v, cost))
        time_taken = [inf] * n
        starting_point = [(0,k - 1)]
        heapify(starting_point)
        while starting_point:
            cost, front = heappop(starting_point)
            time_taken[front] = min(cost, time_taken[front])
            for v, new_cost in graph[front]:
                if cost + new_cost < time_taken[v]:
                    heappush(starting_point, (cost + new_cost, v))
        for i in range(n):
            if time_taken[i] == inf:
                return -1
        return max(time_taken)
