# Problem: H - Dominoes - https://codeforces.com/gym/589822/problem/H

import sys
from math import gcd
from collections import Counter, defaultdict
from functools import cmp_to_key

input = sys.stdin.readline
output = sys.stdout.write

INT = lambda: int(input().strip())
INTS = lambda: list(map(int, input().split()))
LIST = lambda: list(map(int, input().split()))
LINE = lambda: input().strip()
MATRIX = lambda n, m: [input() for _ in range(n)]
MATRIX2 = lambda n, m: [list(map(int, input().split())) for _ in range(n)]

def prefixSum2D(matrix,n,m):
    prefix = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(n):
        for j in range(m):
            prefix[i+1][j+1]=matrix[i][j]+prefix[i][j + 1]+prefix[i + 1][j] - prefix[i][j]

    return prefix

def solve():
    n, m = INTS()
    matrix = MATRIX(n, m)
    horizontal_sum = [[0] * m for _ in range(n)]
    vertical_sum = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if j > 0 and matrix[i][j] == matrix[i][j - 1] and matrix[i][j] == '.':
                horizontal_sum[i][j] = 1
            if i > 0 and matrix[i][j] == matrix[i - 1][j] and matrix[i][j] == '.':
                vertical_sum[i][j] = 1

    horizontal_sum = prefixSum2D(horizontal_sum, n, m)
    vertical_sum = prefixSum2D(vertical_sum, n, m)
    
    q = INT()
    queries = MATRIX2(q, 4)

    for x1, y1, x2, y2 in queries:
        horizontal = horizontal_sum[x2][y2] - horizontal_sum[x2][y1]
        if x1 - 1 >= 0:
            horizontal += horizontal_sum[x1 - 1][y1] - horizontal_sum[x1 - 1][y2]
        
        vertical = vertical_sum[x2][y2] - vertical_sum[x1][y2]
        if y1 - 1 >= 0:
            vertical += vertical_sum[x1][y1 - 1] - vertical_sum[x2][y1 - 1]
        
        answer = horizontal + vertical

        print(answer)

def main():
    solve()

if __name__ == '__main__':
    main()
