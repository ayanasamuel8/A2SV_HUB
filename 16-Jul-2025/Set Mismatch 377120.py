# Problem: Set Mismatch - https://leetcode.com/problems/set-mismatch/description/

class Solution:
    def cycleSort(self, nums):
        start = 0
        while start < len(nums):
            if nums[start] != start + 1 and nums[start] != nums[nums[start] - 1]:
                val = nums[start] - 1
                nums[start], nums[val] = nums[val], val + 1
                continue
            start += 1
    def findErrorNums(self, nums: List[int]) -> List[int]:
        self.cycleSort(nums)
        for idx, val in enumerate(nums):
            if idx != val - 1:
                return [val, idx + 1]
