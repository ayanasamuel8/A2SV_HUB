# Problem: Minimum Height Trees - https://leetcode.com/problems/minimum-height-trees/

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        leaves = deque()
        for i in range(n):
            if len(graph[i]) <= 1:
                leaves.append(i)
        
        rem_nodes = n
        while rem_nodes > 2:
            size = len(leaves)
            rem_nodes -= size
            for _ in range(size):
                leaf = leaves.popleft()
                nbr = graph[leaf].pop()
                graph[nbr].remove(leaf)
                if len(graph[nbr]) == 1:
                    leaves.append(nbr)
        return list(leaves)