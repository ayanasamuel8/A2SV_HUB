# Problem: Count Subarrays With Fixed Bounds - https://leetcode.com/problems/count-subarrays-with-fixed-bounds/

class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        n = len(nums)
        last_min = -1
        last_max = -1
        left = 0
        subarray_count = 0

        for i in range(n):
            if nums[i] < minK or nums[i] > maxK:
                last_min = -1
                last_max = -1
                left = i + 1
                continue
            if nums[i] == minK: last_min = i
            if nums[i] == maxK: last_max = i
            if last_min != -1 and last_max != -1:
                subarray_count += min(last_min, last_max) - left + 1
        return subarray_count