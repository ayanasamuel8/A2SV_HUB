# Problem: Missing Number - https://leetcode.com/problems/missing-number/description/

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        nums.append(-1)
        start = 0
        while start < n:
            idx = nums[start]
            if idx < 0 or idx == start:
                start += 1
            else:
                nums[start], nums[idx] = nums[idx], nums[start]
        for i in range(n + 1):
            if nums[i] == -1:
                return i
