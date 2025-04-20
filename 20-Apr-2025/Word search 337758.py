# Problem: Word search - https://leetcode.com/problems/word-search/

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n, m = len(board), len(board[0])
        drxn = [[0, -1], [-1, 0], [0, 1], [1, 0]]

        def inBound(newx, newy):
            return 0 <= newx < n and 0 <= newy < m

        def dfs(curr, x, y, visited):
            if curr == len(word):
                return True
            for dx, dy in drxn:
                newx, newy = x + dx, y + dy
                if inBound(newx, newy) and board[newx][newy] == word[curr] and (newx, newy) not in visited:
                    visited.add((newx, newy))
                    if dfs(curr + 1, newx, newy, visited):
                        return True
                    visited.remove((newx, newy))
            return False
        
        for i in range(n):
            for j in range(m):
                visited = set([(i, j)])
                if board[i][j] == word[0]:
                    if dfs(1, i, j, visited):
                        return True
        
        return False