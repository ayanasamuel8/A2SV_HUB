# Problem: Missing Number - https://leetcode.com/problems/missing-number/description/

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        return reduce(lambda a,b:a ^ b, nums + list(range(len(nums) + 1)))