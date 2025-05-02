# Problem: Strange Printer II - https://leetcode.com/problems/strange-printer-ii/

class Solution:
    def construct(self, color, graph, indeg, start_row, end_row, start_col, end_col, grid):
        n,m = len(grid), len(grid[0])
        for i in range(start_row, end_row + 1):
            for j in range(start_col, end_col + 1):
                curr = grid[i][j]
                if curr != color and color not in graph[curr]:
                    graph[curr].add(color)
                    indeg[color] += 1


    def isPrintable(self, targetGrid: List[List[int]]) -> bool:
        start_row, start_col = defaultdict(lambda: inf), defaultdict(lambda: inf)
        end_row, end_col = defaultdict(int), defaultdict(int)
        graph = defaultdict(set)
        indeg = defaultdict(int)

        n, m = len(targetGrid), len(targetGrid[0])
        for i in range(n):
            for j in range(m):
                curr = targetGrid[i][j]
                start_row[curr] = min(start_row[curr], i)
                end_row[curr] = max(end_row[curr], i)
                start_col[curr] = min(start_col[curr], j)
                end_col[curr] = max(end_col[curr], j)
        colors = set()
        for row in targetGrid:
            colors.update(set(row))
        

        for color in colors:
            self.construct(color, graph, indeg, start_row[color], end_row[color], start_col[color], end_col[color], targetGrid)
        
        q = deque()
        for color in colors:
            if indeg[color] == 0:
                q.append(color)
        topo_sorted = []
        while q:
            u = q.popleft()
            topo_sorted.append(u)
            for v in graph[u]:
                indeg[v] -= 1
                if indeg[v] == 0:
                    q.append(v)
        return len(topo_sorted) == len(colors)