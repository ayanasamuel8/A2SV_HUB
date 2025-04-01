# Problem: Solving Questions with Brainpower - https://leetcode.com/problems/solving-questions-with-brainpower/

class Solution:
    def calculateDepth(self, idx, questions):
        if idx >= len(questions):
            return 0
        if self.dp[idx] != -1:
            return self.dp[idx]
            
        take = questions[idx][0] + self.calculateDepth(idx + questions[idx][1] + 1, questions)
        skip = self.calculateDepth(idx + 1, questions)
        self.dp[idx] = max(take, skip)
        return self.dp[idx]
        
    def mostPoints(self, questions: List[List[int]]) -> int:
        self.dp = [-1] * len(questions)
        self.calculateDepth(0, questions)
        return self.dp[0]