# Problem: Matrix Diagonal Sum - https://leetcode.com/problems/matrix-diagonal-sum/description/

class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        total = 0

        for i in range(n):
            total += mat[i][i]
            total += mat[i][n - i - 1]
        return (total - ((n % 2) * mat[n//2][n//2]))