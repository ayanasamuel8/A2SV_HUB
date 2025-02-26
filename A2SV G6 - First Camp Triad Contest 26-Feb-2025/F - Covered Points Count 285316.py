# Problem: F - Covered Points Count - https://codeforces.com/gym/589822/problem/F

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
    n= INT()
    ranges = MATRIX(n, 2)
    result = [0] * (n + 1)
    hashmap = defaultdict(int)

    for i, j in ranges:
        hashmap[i] += 1
        hashmap[j + 1] -= 1

    sorted_range = sorted(hashmap.items())
    running_sum = 0
    prev = sorted_range[0][0]
    for i in range(0,len(sorted_range)):
        result[running_sum] += sorted_range[i][0] - prev
        running_sum += sorted_range[i][1]
        prev = sorted_range[i][0]
    output(f"{' '.join(map(str,result[1:]))}")


def main():
    solve()

if __name__ == '__main__':
    main()
