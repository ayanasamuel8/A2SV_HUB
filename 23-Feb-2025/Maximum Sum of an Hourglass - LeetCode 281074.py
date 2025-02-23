# Problem: Maximum Sum of an Hourglass - LeetCode - https://leetcode.com/problems/maximum-sum-of-an-hourglass/description/

class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        n,m = len(grid), len(grid[0])
        ans = 0

        for i in range(n):
            for j in range(1,m):
                grid[i][j] += grid[i][j - 1]
        
        for i in range(n-2):
            for j in range(2,m):
                upper_sum = grid[i][j] - grid[i][j - 3] if j >= 3 else grid[i][j]
                lower_sum = grid[i + 2][j] - grid[i + 2][j - 3] if j>=3 else grid[i + 2][j]
                middle_element = grid[i + 1][j - 1] - grid[i + 1][j - 2]
                total = upper_sum + lower_sum + middle_element
                ans = max(ans,total)
        
        return ans