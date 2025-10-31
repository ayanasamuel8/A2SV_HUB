# Problem: The Two Sneaky Numbers of Digitville - https://leetcode.com/problems/the-two-sneaky-numbers-of-digitville/description

class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        cntr = Counter(nums)
        ans = []
        for key, val in cntr.items():
            if val >= 2:
                ans.append(key)
        return ans