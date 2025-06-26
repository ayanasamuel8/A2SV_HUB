# Problem: Rotate Image - https://leetcode.com/problems/rotate-image/

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n//2):
            for j in range(ceil(n/2)):
                first = matrix[i][j]
                second = matrix[j][n-i-1]
                third = matrix[n-i-1][n-j-1]
                fourth = matrix[n-j-1][i]
                matrix[i][j] = fourth
                matrix[j][n-i-1] = first
                matrix[n-i-1][n-j-1] = second
                matrix[n-j-1][i] = third