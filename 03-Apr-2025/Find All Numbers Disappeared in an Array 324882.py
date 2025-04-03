# Problem: Find All Numbers Disappeared in an Array - https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/description/

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        cycle = [-1] * (n:= len(nums))

        for i in nums:
            if i - 1 < n:
                cycle[i - 1] = i
        ans = []
        for i in range(n):
            if cycle[i] != i + 1:
                ans.append(i + 1)
        
        return ans
