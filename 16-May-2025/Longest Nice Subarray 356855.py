# Problem: Longest Nice Subarray - https://leetcode.com/problems/longest-nice-subarray/

class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        max_len = left = 0
        n = len(nums)
        total = 0

        for right in range(n):
            while total & nums[right] > 0:
                total ^= nums[left]
                left += 1
            total |= nums[right]
            max_len = max(max_len, right - left + 1)
        return max_len