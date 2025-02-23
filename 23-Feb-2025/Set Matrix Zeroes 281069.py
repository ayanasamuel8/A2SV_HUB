# Problem: Set Matrix Zeroes - https://leetcode.com/problems/set-matrix-zeroes/

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n,m = len(matrix), len(matrix[0])

        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    for row in range(n):
                        if matrix[row][j] != 0:
                            matrix[row][j] = '0'
                    for col in range(m):
                        if matrix[i][col] != 0:
                            matrix[i][col] = '0'
        
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == '0':
                    matrix[i][j] = 0