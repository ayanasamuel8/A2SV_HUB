# Problem: First Missing Positive - https://leetcode.com/problems/first-missing-positive/description/

class Solution:
    def cycleSort(self, nums):
        i = 0
        while i < len(nums):
            if nums[i] - 1 != i and 0 < nums[i] <= len(nums) and nums[i] != nums[nums[i] - 1]:
                before = nums[i] - 1
                nums[before], nums[i] = nums[i], nums[before]
            else:
                i += 1

    def firstMissingPositive(self, nums: List[int]) -> int:
        self.cycleSort(nums)
        for i in range(len(nums)):
            if nums[i] - 1 != i:
                return i + 1
        return len(nums) + 1