# Problem: N-Queens - https://leetcode.com/problems/n-queens/description/

class Solution:

    def backTrack(self, row, n):
        if row >= n:
            possible = []
            for i in self.board:
                possible.append(''.join(i))
            self.result.append(possible)
        
        for i in range(n):
            if i not in self.cols and row - i not in self.diagonal and row + i not in self.secondary:
                self.cols.add(i)
                self.diagonal.add(row - i)
                self.secondary.add(row + i)
                self.board[row][i] = 'Q'
                self.backTrack(row + 1, n)
                self.board[row][i] = '.'
                self.cols.remove(i)
                self.diagonal.remove(row - i)
                self.secondary.remove(row + i)


    def solveNQueens(self, n: int) -> List[List[str]]:
        self.result = []
        self.board = [['.'] * n for _ in range(n)]
        self.cols = set()
        self.diagonal = set()
        self.secondary = set()
        self.backTrack(0, n)
        return self.result