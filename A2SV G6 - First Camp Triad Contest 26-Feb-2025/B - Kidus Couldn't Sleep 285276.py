# Problem: B - Kidus Couldn't Sleep - https://codeforces.com/gym/589822/problem/B

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

def prefixSum(array, n):
    prefix_sum = [0]*(n + 1)

    for i in range(n):
        prefix_sum[i + 1] = prefix_sum[i] + array[i]

    return prefix_sum

def solve():
    n, k = INTS()
    array = LIST()
    comulative_sum = 0

    prefix = prefixSum(array, n)

    for i in range(k,n + 1):
        comulative_sum += prefix[i] - prefix[i - k]
    output(f"{comulative_sum / (n - k + 1)}")
        


def main():
    solve()

if __name__ == '__main__':
    main()
