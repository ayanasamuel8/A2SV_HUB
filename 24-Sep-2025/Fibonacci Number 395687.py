# Problem: Fibonacci Number - https://leetcode.com/problems/fibonacci-number/

class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
             return 1

        dp = [-inf] * (n + 1)
        dp[0] = 0
        dp[1] = 1
        def fibo(i):
            if dp[i] != -inf:
                return dp[i]
            dp[i] = fibo(i - 1) + fibo(i - 2)
            return dp[i]

        return fibo(n)