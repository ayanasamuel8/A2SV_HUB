# Problem: Score of Parentheses - https://leetcode.com/problems/score-of-parentheses/

class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        bracket_count = defaultdict(int)
        count = 0
        for i in s:
            if i == '(':
                if not stack: 
                    stack.append(1)
                else: 
                    stack.append(stack[-1] + 1)
            else:
                if stack:
                    back = stack.pop()
                    if bracket_count[back + 1] > 0:
                        bracket_count[back] += bracket_count[back + 1] * 2
                        del bracket_count[back + 1]
                    else: bracket_count[back] += 1
                    count = max(bracket_count[back], count)
        return count