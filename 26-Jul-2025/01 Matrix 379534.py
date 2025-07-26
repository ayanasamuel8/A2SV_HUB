# Problem: 01 Matrix - https://leetcode.com/problems/01-matrix/

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        q = deque()
        n = len(mat)
        m = len(mat[0])
        ans = [[inf] * m for _ in range(n)]
        dirs_4 = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        for i in range(n):
            for j in range(m):
                if mat[i][j] == 0:
                    ans[i][j] = 0
                    q.append([i, j, 1])
        
        def inBound(x, y): return 0 <= x < n and 0 <= y < m
        
        while q:
            u, v, cost = q.popleft()
            for du, dv in dirs_4:
                nu = u + du
                nv = v + dv
                if inBound(nu, nv) and cost < ans[nu][nv]:
                    ans[nu][nv] = cost
                    q.append([nu, nv, cost + 1])
        return ans