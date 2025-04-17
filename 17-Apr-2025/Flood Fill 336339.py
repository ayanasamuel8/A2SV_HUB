# Problem: Flood Fill - https://leetcode.com/problems/flood-fill/

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        n, m = len(image), len(image[0])

        drxn = [[-1, 0], [0, -1], [0, 1], [1, 0]]
        visited = [[False] * m for _ in range(n)]

        def inBound(newx, newy):
            return 0 <= newx < n and 0 <= newy < m
        
        main_color = image[sr][sc]
        active_cell = deque([(sr, sc)])
        
        while active_cell:
            x, y = active_cell.popleft()
            image[x][y] = color
            for dx, dy in drxn:
                newx, newy = x + dx, y + dy
                if inBound(newx, newy) and not visited[newx][newy] and image[newx][newy] == main_color:
                    visited[newx][newy] = True
                    active_cell.append((newx, newy))
        
        return image