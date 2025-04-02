# Problem: Path with Maximum Probability - https://leetcode.com/problems/path-with-maximum-probability/

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        adj = defaultdict(list)
        for i in range(len(edges)):
            u, v = edges[i]
            prob = succProb[i]
            if prob == 0:
                continue
            log_prob = -math.log10(prob)
            adj[u].append((v, log_prob))
            adj[v].append((u, log_prob))
        
        heap = []
        heapq.heappush(heap, (0, start_node))
        
        best_prob = [float('inf')] * n
        best_prob[start_node] = 0
        
        while heap:
            current_log, node = heapq.heappop(heap)
            
            if current_log > best_prob[node]:
                continue
                
            if node == end_node:
                return 10 ** -current_log
            
            for v, log_p in adj[node]:
                new_log = current_log + log_p
                if new_log < best_prob[v]:
                    best_prob[v] = new_log
                    heapq.heappush(heap, (new_log, v))
        
        return 0