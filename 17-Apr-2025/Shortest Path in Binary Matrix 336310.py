# Problem: Shortest Path in Binary Matrix - https://leetcode.com/problems/shortest-path-in-binary-matrix/description/

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        drxn = [[-1, 0], [0, -1], [-1, -1], [1, 0], [0, 1], [1, 1], [-1, 1], [1, -1]]

        min_heap = [(1, (0, 0))]
        heapq.heapify(min_heap)

        def inBound(new_row, new_col):
            return 0 <= new_row < n and 0 <= new_col < m
        
        if grid[0][0]:
            return -1
        
        grid[0][0] = 1
        
        while min_heap:
            cost, (row, col) = heapq.heappop(min_heap)
            if row == n - 1 and col == n - 1:
                return cost
            for delta_row, delta_col in drxn:
                new_row, new_col = row + delta_row, col + delta_col
                if inBound(new_row, new_col) and not grid[new_row][new_col]:
                    grid[new_row][new_col] = 1
                    heapq.heappush(min_heap, (cost + 1, (new_row, new_col)))
        return -1