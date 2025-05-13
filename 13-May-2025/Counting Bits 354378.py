# Problem: Counting Bits - https://leetcode.com/problems/counting-bits/

class Solution:
    def setBit(self, n):
        ans = 0
        while n:
            ans += n & 1
            n >>= 1
        return ans
    def countBits(self, n: int) -> List[int]:
        result = []
        for i in range(n + 1):
            result.append(self.setBit(i))
        return result