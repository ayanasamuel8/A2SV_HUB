# Problem: Matrix Block Sum - https://leetcode.com/problems/matrix-block-sum/

class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        n, m = len(mat), len(mat[0])
        def prefixSum2D():
            prefix = [[0] * (m + 1) for _ in range(n + 1)]

            for i in range(n):
                for j in range(m):
                    prefix[i+1][j+1]=mat[i][j]+prefix[i][j + 1]+prefix[i + 1][j] - prefix[i][j]

            return prefix
        
        prefix_sum = prefixSum2D()
        result = [[0] * m for _ in range(n)]

        for i in range(n):
            for j in range(m):
                r1 = max(0, i - k)
                c1 = max(0, j - k)
                r2 = min(n, i + k + 1)
                c2 = min(m, j + k + 1)
                result[i][j] = prefix_sum[r2][c2] - prefix_sum[r2][c1] - prefix_sum[r1][c2] + prefix_sum[r1][c1]
        return result