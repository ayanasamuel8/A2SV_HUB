# Problem: Largest Perimeter Triangle - https://leetcode.com/problems/largest-perimeter-triangle/

class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        for i in range(n - 1, 1, -1):
            if nums[i- 1] + nums[i - 2] > nums[i]:
                return nums[i] + nums[i - 1] + nums[i - 2] 
        return 0