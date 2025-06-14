# Problem: Longest Subarray of 1's After Deleting One Element - https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        total_ones = 0
        max_ones = 0
        zero_seen = False
        zero_never_seen = True
        left = 0
        length = len(nums)

        for right in range(length):
            if nums[right] == 0:
                while zero_seen:
                    total_ones -= nums[left]
                    zero_seen = bool(nums[left])
                    left += 1
                zero_seen = True
                zero_never_seen = False
            total_ones += nums[right]
            max_ones = max(max_ones, total_ones)
        
        return max_ones - int(zero_never_seen)