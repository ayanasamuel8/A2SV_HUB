# Problem: A. Beautiful Matrix - https://codeforces.com/problemset/problem/263/A

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
MATRIX = lambda n, m: [list(map(int, input().split())) for _ in range(n)]


def solve():
    matrix = MATRIX(5,5)

    for i in range(5):
        for j in range(5):
            if matrix[i][j] == 1:
                output(f"{abs(2 - i) + abs(2 - j)}\n")
                break
    

def main():
    solve()

if __name__ == '__main__':
    main()
