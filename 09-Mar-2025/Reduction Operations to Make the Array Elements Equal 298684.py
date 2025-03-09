# Problem: Reduction Operations to Make the Array Elements Equal - https://leetcode.com/problems/reduction-operations-to-make-the-array-elements-equal/

class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        total = 0
        dp = {nums[0] : 0}
        for i in range(n):
            element = nums[i]
            if element not in dp:
                dp[element] = dp[nums[i - 1]] + 1
            total += dp[element]
        return total