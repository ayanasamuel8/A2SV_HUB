# Problem: Longest Subarray With Maximum Bitwise AND - https://leetcode.com/problems/longest-subarray-with-maximum-bitwise-and/

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        max_and = max(nums)
        max_len = 0
        left = 0
        n = len(nums)
        for right in range(n):
            if nums[right] != max_and:
                left = right + 1
                continue
            max_len = max(max_len, right - left + 1)
        return max_len