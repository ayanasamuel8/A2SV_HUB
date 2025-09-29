# Problem: Target Sum - https://leetcode.com/problems/target-sum/

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}
        def dp(idx, tar):
            if idx < 0:
                return int(tar == 0)
            if (idx, tar) in memo:
                return memo[(idx, tar)]
            minus = dp(idx - 1, tar - nums[idx])
            add = dp(idx - 1, tar + nums[idx])
            memo[(idx, tar)] = minus + add
            return minus + add
        return dp(len(nums) - 1, target)