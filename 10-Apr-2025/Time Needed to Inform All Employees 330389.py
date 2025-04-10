# Problem: Time Needed to Inform All Employees - https://leetcode.com/problems/time-needed-to-inform-all-employees/

class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        answer = [0] * (n)
        adj = defaultdict(list)

        for i in range(n):
            adj[manager[i]].append(i)
        
        def dfs(node):
            timeTaken = 0
            for nbr in adj[node]:
                timeTaken = max(timeTaken, dfs(nbr))
            return timeTaken + informTime[node]

        return dfs(headID)