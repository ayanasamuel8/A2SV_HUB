# Problem: Find First and Last Position of Element in Sorted Array - https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left, right = 0, len(nums) - 1
        found_left = found_right = -1

        while left <= right:
            mid = left + (right - left) // 2 
            if nums[mid] == target:
                found_left = mid
            if nums[mid] >= target:
                right = mid - 1
            else:
                left = mid + 1

        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2 
            if nums[mid] == target:
                found_right = mid
            if nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1

        return [found_left, found_right]
        
            
        
