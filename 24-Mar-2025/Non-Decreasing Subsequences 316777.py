# Problem: Non-Decreasing Subsequences - https://leetcode.com/problems/non-decreasing-subsequences/description/

class Solution:
    def backTrack(self, path, nums, idx,copy):
        if len(path) > 1 and copy:
            self.result.add(tuple(path.copy()))
        if idx == len(nums):
            return

        if not path or path[-1] <= nums[idx]:
            path.append(nums[idx])
            self.backTrack(path, nums, idx + 1, True)
            path.pop()
        self.backTrack(path, nums, idx + 1, False)

    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        self.result = set()
        ans = []
        self.backTrack([], nums, 0, False)
        for i in self.result:
            ans.append(list(i))
        return ans