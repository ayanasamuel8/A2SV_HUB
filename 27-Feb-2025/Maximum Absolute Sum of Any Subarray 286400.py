# Problem: Maximum Absolute Sum of Any Subarray - https://leetcode.com/problems/maximum-absolute-sum-of-any-subarray/

class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        min_sum = max_sum = current_min = current_max = 0

        for i in nums:
            current_min = min(i, i + current_min)
            current_max = max(i, i + current_max)
            min_sum = min(min_sum, current_min)
            max_sum = max(max_sum, current_max)
        return max(max_sum, abs(min_sum))