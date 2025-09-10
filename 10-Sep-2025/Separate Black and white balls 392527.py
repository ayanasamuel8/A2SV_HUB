# Problem: Separate Black and white balls - https://leetcode.com/problems/separate-black-and-white-balls/

class Solution:
    def minimumSteps(self, s: str) -> int:
        left = 0
        n = len(s)
        total = 0
        for right in range(n):
            if s[right] == '1':
                continue
            total += right - left
            left += 1
        return total