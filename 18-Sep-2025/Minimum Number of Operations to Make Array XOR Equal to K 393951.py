# Problem: Minimum Number of Operations to Make Array XOR Equal to K - https://leetcode.com/problems/minimum-number-of-operations-to-make-array-xor-equal-to-k/

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        xor = reduce(lambda a, b: a ^ b, nums)
        s  = bin(xor)[2:] 
        s2 = bin(k)[2:]

        n = max(len(s), len(s2))
        s  = s.zfill(n)
        s2 = s2.zfill(n)

        cnt = 0
        for i in range(n):
            cnt += s[i] != s2[i]
        return cnt