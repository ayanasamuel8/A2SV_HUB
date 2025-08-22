# Problem: Pow(x, n) - https://leetcode.com/problems/powx-n/

class Solution:
    def myPow(self, x: float, n: int) -> float:
        def posPow(x,n):
            if n == 0: return 1
            if n == 1: return x
            half = posPow(x, n//2)
            if n % 2:
                return x * half * half
            else:
                return half * half
        if n < 0:
            return 1/posPow(x,-n)
        return posPow(x,n)