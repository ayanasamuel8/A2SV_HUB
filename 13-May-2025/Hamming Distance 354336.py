# Problem: Hamming Distance - https://leetcode.com/problems/hamming-distance/

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        ans = 0
        while x or y:
            if (x & 1 and not y & 1) or (not x & 1 and y & 1):
                ans += 1
            if x:
                x>>=1
            if y:
                y >>= 1
        return ans