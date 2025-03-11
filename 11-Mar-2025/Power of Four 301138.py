# Problem: Power of Four - https://leetcode.com/problems/power-of-four/

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n == 4 or n == 1: return True
        if n % 4 != 0 or n <= 0: return False
        return self.isPowerOfFour(n//4)