# Problem: Number of Provinces - https://leetcode.com/problems/number-of-provinces/

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = [[False] * n for _ in range(n)]
        def markConnected(row):
            for col in range(n):
                if not visited[row][col] and isConnected[row][col] == 1:
                    visited[row][col] = True
                    markConnected(col)
        cnt = 0

        for row in range(n):
            for col in range(n):
                if isConnected[row][col] == 1 and not visited[row][col]:
                    visited[row][col] = True
                    markConnected(row)
                    markConnected(col)
                    cnt += 1
        return cnt