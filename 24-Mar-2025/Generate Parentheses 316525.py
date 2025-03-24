# Problem: Generate Parentheses - https://leetcode.com/problems/generate-parentheses/description/

class Solution:
    def backTrack(self, cnt, n, path):
        if len(path) // 2 == n:
            if cnt == 0:
                self.result.append(''.join(path))
            return
        if len(path) != 2 * n - 1:
            path.append('(')
            self.backTrack(cnt + 1, n, path)
            path.pop()
        if cnt:
            path.append(')')
            self.backTrack(cnt - 1, n, path)
            path.pop()

    def generateParenthesis(self, n: int) -> List[str]:
        self.result = []
        self.backTrack(0, n, [])
        return self.result