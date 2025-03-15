# Problem: Count Good Numbers - https://leetcode.com/problems/count-good-numbers/

class Solution:
    def myPow(self, exp, base, mod, result):
        if exp == 0: return result
        if exp & 1:
            result = (result * base) % mod
        base = (base * base) % mod
        return self.myPow(exp>>1, base,mod, result)
    def countGoodNumbers(self, n: int) -> int:
        MOD = int(1e9 + 7)
        odd_indecies = n//2
        even_indecies = n - odd_indecies

        odd = self.myPow(odd_indecies, 4, MOD,1)
        even = self.myPow(even_indecies, 5, MOD,1)

        return odd * even % MOD