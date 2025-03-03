# Problem: Jump Game - https://leetcode.com/problems/jump-game/

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        curr_max = nums[0]
        for i in range(n - 1):
            curr_max = max(curr_max, nums[i])
            if curr_max == 0: return False
            curr_max -= 1
        return True