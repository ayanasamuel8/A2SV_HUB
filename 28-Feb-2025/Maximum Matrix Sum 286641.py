# Problem: Maximum Matrix Sum - https://leetcode.com/problems/maximum-matrix-sum/description/?envType=problem-list-v2&envId=matrix

class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        num_negative, min_el = 0, float('inf')
        commulative_sum = 0
        n,m = len(matrix), len(matrix[0])

        for i in range(n):
            for j in range(m):
                commulative_sum += abs(matrix[i][j])
                if matrix[i][j] < 0:
                    num_negative += 1 
                min_el = min(min_el,abs(matrix[i][j]))
        if num_negative % 2:
            commulative_sum -= 2 * (min_el)
        return commulative_sum