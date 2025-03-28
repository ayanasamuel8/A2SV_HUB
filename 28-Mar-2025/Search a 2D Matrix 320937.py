# Problem: Search a 2D Matrix - https://leetcode.com/problems/search-a-2d-matrix/

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left, right = 0, len(matrix) * (m := len(matrix[0])) - 1

        while left <= right:
            mid = left + (right - left) // 2

            row, col = mid // m, mid % m
            if matrix[row][col] == target:
                return True
            if matrix[row][col] > target:
                right = mid - 1
            else:
                left = mid + 1

        return False