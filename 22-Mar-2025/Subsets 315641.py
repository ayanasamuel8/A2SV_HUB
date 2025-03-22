# Problem: Subsets - https://leetcode.com/problems/subsets/

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        def backTrack(idx, path):
            result.append(path.copy())
            if idx == len(nums):
                return
            for i in range(idx, len(nums)):
                path.append(nums[i])
                backTrack(i + 1, path)
                path.pop()
        backTrack(0, [])
        return result