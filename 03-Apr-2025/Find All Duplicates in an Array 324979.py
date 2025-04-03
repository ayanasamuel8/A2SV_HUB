# Problem: Find All Duplicates in an Array - https://leetcode.com/problems/find-all-duplicates-in-an-array/description/

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        start = 0
        n = len(nums)
        ans = set()
        while start < n:
            correct_idx = nums[start] - 1
            if correct_idx == start:
                start += 1
            elif nums[start] == nums[correct_idx]:
                ans.add(nums[start])
                start += 1
            else:
                nums[start], nums[correct_idx] = nums[correct_idx], nums[start]
        return list(ans)
