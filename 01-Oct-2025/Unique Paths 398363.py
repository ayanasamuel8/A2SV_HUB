# Problem: Unique Paths - https://leetcode.com/problems/unique-paths/

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0] * m for _ in range(n)]
        dp[n - 1][m - 1] = 1

        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                right = dp[i][j + 1] if j + 1 < m else 0
                down = dp[i + 1][j] if i + 1 < n else 0
                if i != n - 1 or j != m - 1:
                    dp[i][j] = right + down
                
        return dp[0][0]