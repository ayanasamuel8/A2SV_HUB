# Problem: Separate Black and white balls - https://leetcode.com/problems/separate-black-and-white-balls/

class Solution:
    def minimumSteps(self, s: str) -> int:
        ones = 0
        n = len(s)
        total = 0
        for i in range(n):
            if s[i] == '1':
                ones += 1
                continue
            total += ones
        return total