# Problem: Odd Subarrays - https://codeforces.com/problemset/problem/1686/B

import sys, math
from collections import Counter, defaultdict,deque
from functools import cmp_to_key

input = sys.stdin.readline
output = sys.stdout.write

INT = lambda: int(input().strip())
INTS = lambda: list(map(int, input().split()))
LIST = lambda: list(map(int, input().split()))
LINE = lambda: input().strip()
MATRIX = lambda n, m: [list(map(int, input().split())) for _ in range(n)]

def solve():
    n = INT()
    nums = LIST()

    pas = False
    count = 0

    for r in range(1,n):
        if pas: 
            pas = False
            continue
        if nums[r - 1] > nums[r]:
            count += 1
            pas = True
    output(f"{count}\n")

def main():
    T = INT()
    for _ in range(T):
        solve()

if __name__ == '__main__':
    main()
