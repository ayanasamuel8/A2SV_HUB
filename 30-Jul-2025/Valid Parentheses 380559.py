# Problem: Valid Parentheses - https://leetcode.com/problems/valid-parentheses

class Solution:
    def isValid(self, s: str) -> bool:
        open_ = {'(', '{', '['}
        vals = {'(' : ')', '{' : '}', '[' : ']'}
        stack = []
        for i in s:
            if i not in open_:
                if not stack or vals[stack[-1]] != i:
                    return False
                stack.pop()
            else:
                stack.append(i)
        return not stack