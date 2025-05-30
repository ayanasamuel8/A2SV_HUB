# Problem: Range Sum Query 2D - Immutable - https://leetcode.com/problems/range-sum-query-2d-immutable/

class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        n,m = len(matrix), len(matrix[0])
        self.prefix_2D = [[0]*(m+1)for _ in range(n+1)]

        for i in range(n):
            for j in range(m):
                self.prefix_2D[i+1][j+1] = self.prefix_2D[i+1][j] + matrix[i][j]
        
        for i in range(n):
            for j in range(m):
                self.prefix_2D[i+1][j+1] = self.prefix_2D[i][j+1] + self.prefix_2D[i+1][j+1]
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return (self.prefix_2D[row2+1][col2+1] - self.prefix_2D[row1][col2+1]) - (self.prefix_2D[row2+1][col1] - self.prefix_2D[row1][col1])


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)