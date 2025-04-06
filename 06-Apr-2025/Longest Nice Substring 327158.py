# Problem: Longest Nice Substring - https://leetcode.com/problems/longest-nice-substring/

class Solution:
    def divide(self, s):
        if not s:
            return ''
        chars = set(s)
        for i in range(len(s)):
            if s[i].swapcase() not in s:
                left = self.divide(s[:i])
                right = self.divide(s[i + 1:])
                return left if len(left) >= len(right) else right
                break
        else:
            return s
        return ''
    def longestNiceSubstring(self, s: str) -> str:
        ans = self.divide(s)
        return ans