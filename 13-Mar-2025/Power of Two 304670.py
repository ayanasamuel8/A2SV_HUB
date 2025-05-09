# Problem: Power of Two - https://leetcode.com/problems/power-of-two/

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 1: return True
        if n % 2 or n == 0: return False
        return self.isPowerOfTwo(n//2)