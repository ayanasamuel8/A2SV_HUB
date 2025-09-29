# Problem: Coin Change - https://leetcode.com/problems/coin-change/

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        memo = {}
        def dp(amount):
            if amount < 0:
                return inf
            if amount == 0:
                return 0
            if amount in memo:
                return memo[amount]
            ans = inf
            for i in range(n):
                ans = min(ans, dp(amount - coins[i]) + 1)
            memo[amount] = ans
            return ans
        ans = dp(amount)
        return ans if ans != inf else -1