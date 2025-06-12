# Problem: Single Number III - https://leetcode.com/problems/single-number-iii/

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        all_xor = reduce(lambda a,b: a ^ b, nums)
        left = inf
        for i in range(33):
            if all_xor & (1 << i):
                left = i
                break
        group1 = 0
        group2 = 0
        for i in nums:
            if i & (1 << left):
                group1 ^= i
            else:
                group2 ^= i
        return [group1, group2]