# Problem: A - Kibr and His Musics - https://codeforces.com/gym/589822/problem/A

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
    n, q = INTS()
    ranges = MATRIX(n, 2)
    queries = LIST()

    running_sum = 0
    index = 0

    for i in queries:
        while index < n and running_sum < i:
            running_sum += (ranges[index][0] * ranges[index][1])
            index += 1
        output(f"{index}\n")


def main():
    solve()

if __name__ == '__main__':
    main()
