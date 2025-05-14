# Problem: Subsets - https://leetcode.com/problems/subsets/

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        n = len(nums)
        for i in range(1 << n):
            arr =[]
            for j in range(n):
                if i & (1 << j):
                    arr.append(nums[j])
            result.append(arr)
        return result