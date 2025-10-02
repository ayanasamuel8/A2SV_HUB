# Problem: Minimum Falling Path Sum - https://leetcode.com/problems/minimum-falling-path-sum/

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        ### Bottom-Up dp
        dp = [inf] * n
        for i in range(n):
            dp[i] = matrix[n - 1][i]
        
        for row in range(n - 2, -1, -1):
            dp_curr = [inf] * n
            for col in range(n):
                dleft = dp[col - 1] if col > 0 else inf
                down = dp[col]
                dright = dp[col + 1] if col < n - 1 else inf
                dp_curr[col] = matrix[row][col] + min(dleft, down, dright)
            dp = dp_curr
        return min(dp)


        ### Top-Down dp
        # memo = {}
        # def dp(row, col):
        #     if row == n - 1:
        #         return matrix[row][col]
        #     if (row, col) in memo:
        #         return memo[(row, col)]
        #     curr = matrix[row][col]
        #     #digonal left
        #     dleft = dp(row + 1, col - 1) if col > 0 else inf
        #     #down
        #     down = dp(row + 1, col)
        #     #diagonal right
        #     dright = dp(row + 1, col + 1) if col < n - 1 else inf
        #     memo[(row, col)] = curr + min(dleft, down, dright)
        #     return memo[(row, col)]
        
        # min_sum = inf
        # for i in range(n):
        #     min_sum = min(min_sum, dp(0, i))
        # return min_sum