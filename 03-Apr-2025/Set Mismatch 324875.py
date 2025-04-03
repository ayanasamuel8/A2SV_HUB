# Problem: Set Mismatch - https://leetcode.com/problems/set-mismatch/description/

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        cycle = [-1] * (n:=len(nums))
        ans = []
        for i in nums:
            if cycle[i - 1] == -1:
                cycle[i - 1] = i - 1
            else:
                ans.append(i)
        for i in range(n):
            if cycle[i] == -1:
                ans.append(i + 1)
        return ans
