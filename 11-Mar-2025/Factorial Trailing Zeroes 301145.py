# Problem: Factorial Trailing Zeroes - https://leetcode.com/problems/factorial-trailing-zeroes/

class Solution:
    def fact(self,n):
        if n <= 1: return n
        return n * self.fact(n -1)
    def trailingZeroes(self, n: int) -> int:
        sys.set_int_max_str_digits(1000000000)
        fact = str(self.fact(n))
        right = len(fact) - 1
        while right > 0 and fact[right] == '0':
            right -= 1
        return len(fact) - right - 1
