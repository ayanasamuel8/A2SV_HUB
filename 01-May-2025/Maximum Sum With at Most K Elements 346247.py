# Problem: Maximum Sum With at Most K Elements - https://leetcode.com/problems/maximum-sum-with-at-most-k-elements/description/

class Solution:
    def maxSum(self, grid: List[List[int]], limits: List[int], k: int) -> int:
        max_heap = []
        n = len(limits)
        m = len(grid[0])
        for i in range(n):
            row_heap = []
            for j in range(m):
                heappush(row_heap, -grid[i][j])
            while limits[i]:
                heappush(max_heap, heappop(row_heap))
                limits[i] -= 1
        total = 0
        while k:
            total -= heappop(max_heap)
            k -= 1
        return total