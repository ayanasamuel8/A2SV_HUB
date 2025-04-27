# Problem: B - The Ethiopian Lakes - https://codeforces.com/gym/602812/problem/B

import threading, sys
def main():
    t = int(input())
    while t:
        t -= 1
        n,m = map(int, input().split())
        grid = []
        for i in range(n):
            inp = list(map(int, input().split()))
            grid.append(inp)
        def inBound(nrow, ncol):
            return 0 <= nrow < n and 0 <= ncol < m
        
        drxn = [[-1,0], [0, -1], [1, 0], [0, 1]]
        visited = [[False] * m for _ in range(n)]
            
        def dfs(row, col):
            cnt = grid[row][col]
            for dx, dy in drxn:
                nrow, ncol = row + dx, col + dy
                if inBound(nrow, ncol) and grid[nrow][ncol] != 0 and not visited[nrow][ncol]:
                    visited[nrow][ncol] = True
                    cnt += dfs(nrow, ncol)
            return cnt
        
        ans = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] != 0 and not visited[i][j]:
                    visited[i][j] = True
                    ans = max(ans, dfs(i,j))
        print(ans)
if __name__ == '__main__':
    
    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1 << 27)

    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()