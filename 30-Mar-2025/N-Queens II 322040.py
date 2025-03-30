# Problem: N-Queens II - https://leetcode.com/problems/n-queens-ii/description/

class Solution:
    def totalNQueens(self, n: int) -> int:
        colseen = set()
        maindiagonal = set()
        secondarydiagonal = set()
        self.count = 0
        def backTrack(row):
            if row >= n:
                return
            for i in range(n):
                if i not in colseen and row - i not in maindiagonal and row + i not in secondarydiagonal:
                    colseen.add(i)
                    maindiagonal.add(row - i)
                    secondarydiagonal.add(row + i)
                    if row == n - 1:
                        self.count += 1
                    backTrack(row + 1)
                    colseen.remove(i)
                    maindiagonal.remove(row - i)
                    secondarydiagonal.remove(row + i)
        backTrack(0)
        return self.count