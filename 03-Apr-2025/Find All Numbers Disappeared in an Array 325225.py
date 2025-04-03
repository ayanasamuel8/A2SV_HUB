# Problem: Find All Numbers Disappeared in an Array - https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/description/

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)

        start = 0
        while start < n:
            idx = nums[start] - 1
            if nums[start] != nums[idx]:
                nums[start], nums[idx] = nums[idx], nums[start]
            else:
                start +=1
        return [i + 1 for i in range(n) if nums[i] != i + 1]
