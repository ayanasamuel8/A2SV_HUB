# Problem: House Robber - https://leetcode.com/problems/house-robber/

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = {}
        def robb(idx):
            if idx >= n:
                return 0
            if idx in dp:
                return dp[idx]
            dp[idx] =  nums[idx] + max(robb(idx + 2), robb(idx + 3))
            return dp[idx]
        return max(robb(0), robb(1))