# Problem: Count Subarrays Where Max Element Appears at Least K Times - https://leetcode.com/problems/count-subarrays-where-max-element-appears-at-least-k-times/

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        left = 0
        largest = max(nums)
        count = maxEl = 0        
        for right in range(len(nums)):
            if nums[right] == largest:
                maxEl += 1
            while maxEl == k:
                if nums[left] == largest:
                    maxEl -= 1
                left += 1
            count += left
        return count