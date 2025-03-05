# Problem: Backspace String Compare - https://leetcode.com/problems/backspace-string-compare/

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack = []
        for i in s:
            if i == '#':
                if stack: 
                    stack.pop()
            else:
                stack.append(i)
        stack_t = []
        for i in t:
            if i == '#':
                if stack_t:
                    stack_t.pop()
            else:
                stack_t.append(i)
        return stack == stack_t
        