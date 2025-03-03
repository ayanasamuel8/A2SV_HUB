# Problem: Red and Blue - https://codeforces.com/contest/1469/problem/B

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

def prefixSum(array, n):
    prefix_sum = [0]*(n + 1)

    for i in range(n):
        prefix_sum[i + 1] = prefix_sum[i] + array[i]

    return prefix_sum

def solve():
    n = INT()
    nums = LIST()
    m = INT()
    nums2 = LIST()
    nums = prefixSum(nums, n)
    nums2 = prefixSum(nums2, m)

    output(f"{max(nums) + max(nums2)}\n")

def main():
    T = INT()
    for _ in range(T):
        solve()

if __name__ == '__main__':
    main()
