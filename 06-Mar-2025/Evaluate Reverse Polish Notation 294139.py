# Problem: Evaluate Reverse Polish Notation - https://leetcode.com/problems/evaluate-reverse-polish-notation/

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        arithmetics = {'+', '-', '/', '*'}
        for i in tokens:
            if i in arithmetics:
                back = stack.pop()
                stack[-1] = str(int(eval(stack[-1] + i + back)))
            else: stack.append(i)
        return int(stack[-1])