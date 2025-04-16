# Problem: Shortest Path with Alternating Colors - https://leetcode.com/problems/shortest-path-with-alternating-colors/description/

class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        RED, BLUE = 0, 1
        adjR = defaultdict(list)
        adjB = defaultdict(list)

        for u,v in redEdges:
            adjR[u].append((v, 0))
        for u,v in blueEdges:
            adjB[u].append((v, 1))
        
        ans = [inf] * n

        queue = deque([((0, -1), 0)])
        processed = [0] * n
        visitedR = [False] * n
        visitedB = [False] * n

        while queue:
            (node, color), level = queue.popleft()
            ans[node] = min(ans[node], level)
            for nbr, col in adjR[node]:
                if col != color and not visitedR[nbr]:
                    visitedR[nbr] = True
                    queue.append(((nbr, col), level + 1))
            for nbr, col in adjB[node]:
                if col != color and not visitedB[nbr]:
                    visitedB[nbr] = True
                    queue.append(((nbr, col), level + 1))
        
        for i in range(n):
            if ans[i] == inf:
                ans[i] = -1
        
        return ans
