# Problem: Expression Add Operators - https://leetcode.com/problems/expression-add-operators/description/

class Solution:
    def check(self, s):
        n = len(s)
        for i in range(1, n - 1):
            if s[i] == '0' and not s[i - 1].isdigit() and s[i + 1].isdigit():
                return False
        return s[0] != '0' or not s[1].isdigit()
        

    def addOperators(self, num: str, target: int) -> List[str]:
        ans = []
        n = len(num)
        def backtrack(idx, ops):
            if idx >= n:
                if self.check(ops) and eval(ops) == target:
                    ans.append(ops)
                return
            backtrack(idx + 1, ops + '+' + num[idx])
            backtrack(idx + 1, ops + '-' + num[idx])
            backtrack(idx + 1, ops + '*' + num[idx])
            backtrack(idx + 1, ops + num[idx])
        backtrack(1, num[0])
        return ans