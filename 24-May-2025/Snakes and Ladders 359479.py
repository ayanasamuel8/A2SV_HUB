# Problem: Snakes and Ladders - https://leetcode.com/problems/snakes-and-ladders/

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        flatened = []
        for i in range(n - 1, -1, -1):
            row = board[i]
            if (n - 1 - i) % 2 == 1:
                row = row[::-1]
            flatened.extend(row)
        
        visited = [False] * (n * n)
        q = deque([0])
        visited[0] = True
        level = 0

        while q:
            for _ in range(len(q)):
                curr = q.popleft()
                if curr == n * n - 1:
                    return level
                for move in range(1, 7):
                    next_pos = curr + move
                    if next_pos >= n * n:
                        continue
                    dest = flatened[next_pos] - 1 if flatened[next_pos] != -1 else next_pos
                    if not visited[dest]:
                        visited[dest] = True
                        q.append(dest)
            level += 1

        return -1
