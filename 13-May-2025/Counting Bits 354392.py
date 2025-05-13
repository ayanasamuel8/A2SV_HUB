# Problem: Counting Bits - https://leetcode.com/problems/counting-bits/

class Solution:
    # def setBit(self, n):
    #     ans = 0
    #     while n:
    #         ans += n & 1
    #         n >>= 1
    #     return ans
    def countBits(self, n: int) -> List[int]:
        result = [0]
        for i in range(1,n + 1):
            result.append(result[i >> 1] + (i & 1))
        return result