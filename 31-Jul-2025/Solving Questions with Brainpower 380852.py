# Problem: Solving Questions with Brainpower - https://leetcode.com/problems/solving-questions-with-brainpower/

class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        max_sofar = [0, inf]
        n = len(questions)
        dp = [0] * n
        for i in range(n - 1, -1 ,-1):
            curr = questions[i][0] + dp[i + questions[i][1] + 1] if (i + questions[i][1] + 1) < n else questions[i][0]
            if max_sofar[0] < curr:
                max_sofar = [curr, i]
            dp[i] = max_sofar[0]
        return dp[0]