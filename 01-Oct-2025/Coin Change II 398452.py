# Problem: Coin Change II - https://leetcode.com/problems/coin-change-ii/

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        memo = {}
        def dp(amnt, i):
            #base cases
            if amnt == 0:
                return 1
            if i >= n:
                return 0
            if (amnt, i) in memo:
                return memo[(amnt, i)]

            #not take the current coin  
            total  = dp(amnt, i + 1)

            #take with possbile number of coins[i]
            if amnt >= coins[i]:
                total += dp(amnt - coins[i], i)
            
            #memoization
            memo[(amnt, i)] = total
                

            return memo[(amnt, i)]

        return dp(amount, 0)