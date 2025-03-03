# Problem: Two City Scheduling - https://leetcode.com/problems/two-city-scheduling/

class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        arr = []
        n = len(costs)
        for i in range(n):
            arr.append([costs[i][0] - costs[i][1], (costs[i][0], costs[i][1])])
        arr.sort()
        total = 0
        for i in range(n//2):
            total += arr[i][1][0] + arr[i + n//2][1][1]
        return total