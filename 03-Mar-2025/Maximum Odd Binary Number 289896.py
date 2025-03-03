# Problem: Maximum Odd Binary Number - https://leetcode.com/problems/maximum-odd-binary-number/

class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        ones = s.count('1')
        length = len(s)
        return '1' * (ones - 1) + '0' * (length - ones) + '1' if ones > 1 else '0' * (length - 1) + '1'