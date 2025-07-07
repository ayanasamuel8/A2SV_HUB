# Problem: The Two Sneaky Numbers of Digitville - https://leetcode.com/problems/the-two-sneaky-numbers-of-digitville/description

class Solution:
    def cycleSort(self, nums):
        start = 0
        while start < len(nums):
            if nums[start] != start and nums[start] != nums[nums[start]]:
                var = nums[start]
                nums[start], nums[var] = nums[var],  var
                continue
            start += 1
    
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        self.cycleSort(nums)
        return nums[-2:]