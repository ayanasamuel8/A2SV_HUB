# Problem: Split a String in Balanced Strings - https://leetcode.com/problems/split-a-string-in-balanced-strings/

class Solution:
    def balancedStringSplit(self, s: str) -> int:
        if 'L' not in s or 'R' not in s: return len(s)
        l = r = 0
        balanced = 0
        for i in s:
            if i == 'L': l += 1
            else : r += 1
            if r == l:
                balanced += 1
        return balanced