# Problem: D - Socialism - https://codeforces.com/gym/589822/problem/D

import sys, math
from functools import cmp_to_key
from collections import Counter, defaultdict

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
    n, x = INTS()
    array = LIST()
    array.sort()
    array = prefixSum(array, n)

    for i in range(n):
        burles = array[-1] - array[i]
        if burles/(n - i) >= x:
            output(f"{n - i}\n")
            break
    else:
        output('0\n')
    

def main():
    t = INT()
    for _ in range(t):
        solve()

if __name__ == '__main__':
    main()
