# Problem: Evaluate Division - https://leetcode.com/problems/evaluate-division/

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        mult = defaultdict(list)
        for idx, (a, b) in enumerate(equations):
            mult[a].append((b, values[idx]))
            mult[b].append((a, 1/values[idx]))
    
        def bfs(start, end):
            q = deque([(start, 1)])
            visited = set([start])
            while q:
                front, cost = q.popleft()
                if front == end:
                    return True, cost
                for v, num in mult[front]:
                    if v not in visited:
                        visited.add(v)
                        q.append((v, cost * num))
            return False, 0
        
        ans = []
        for a,b in queries:
            if a not in mult or b not in mult:
                ans.append(-1)
                continue
            state, m = bfs(a, b)
            if state:
                ans.append(m)
                continue
            ans.append(-1)
        return ans