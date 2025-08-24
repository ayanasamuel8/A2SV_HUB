# Problem: Longest Subarray of 1's After Deleting One Element - https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        if 0 not in nums:
            return n - 1
        
        left = 0
        zero_count = 0
        max_count = 0
        for right in range(n):
            zero_count += nums[right] == 0
            while zero_count > 1:
                zero_count -= nums[left] == 0
                left += 1
            max_count = max(max_count, right - left + 1 if zero_count == 0 else right - left)
        return max_count