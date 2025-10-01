# Problem: Unique Paths - https://leetcode.com/problems/unique-paths/

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0] * m for _ in range(n)]
        #base case filling
        for i in range(n):
            dp[i][m - 1] = 1
        for j in range(m):
            dp[n - 1][j] = 1

        #dp computations
        for i in range(n - 2, -1, -1):
            for j in range(m - 2, -1, -1):
                if i != n - 1 or j != m - 1:
                    #recurrence relations 
                    dp[i][j] = dp[i + 1][j] + dp[i][j + 1]
               
        return dp[0][0]