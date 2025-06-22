# Problem: Predict the Winner - https://leetcode.com/problems/predict-the-winner/

class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [[None] * n for _ in range(n)]

        def recursion(left, right):
            if left == right:
                return nums[left]
            print(left, right)
            if dp[left][right] != None:
                return dp[left][right]
            
            pick_left = nums[left] - recursion(left + 1, right)
            pick_right = nums[right] - recursion(left, right - 1)
            dp[left][right] = max(pick_left, pick_right)
            return dp[left][right]
        
        return recursion(0, n - 1) >= 0
        