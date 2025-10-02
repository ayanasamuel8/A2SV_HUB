# Problem: Solving Questions With Brainpower - https://leetcode.com/problems/solving-questions-with-brainpower/

class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        ### Bottom-up approach
        dp = [-inf] * n
        dp[n - 1] = questions[n - 1][0]
        for i in range(n - 2, -1, -1):
            step = i + questions[i][1] + 1
            solve = questions[i][0] + (
                dp[step] if step < n else 0
            )
            dp[i] = max(solve, dp[i + 1])
        return dp[0]

        ### Top-Down approach
        # memo = {}
        # def dp(idx):
        #     if idx >= n:
        #         return 0
        #     if idx in memo:
        #         return memo[idx]
        #     #not take
        #     not_take = dp(idx + 1)
        #     #take
        #     take = questions[idx][0] + dp(idx + questions[idx][1] + 1)
        #     memo[idx] = max(take, not_take)
        #     return memo[idx]
        # return dp(0)