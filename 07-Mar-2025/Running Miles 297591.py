# Problem: Running Miles - https://codeforces.com/problemset/problem/1826/D

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
    array = []
    array2 = []
    for i in range(n):
        array2.append(nums[i] - i)
    for i in range(n):
        array.append(nums[i] + i)
    for i in range(n -2, -1,-1):
        array2[i] = max(array2[i + 1], array2[i])
    min_el = array[0]
    total = min_el + array2[2] + nums[1]
    for i in range(2,n -1):
        min_el = max(array[i - 1], min_el)
        total = max(total, min_el + array2[i + 1] + nums[i])
    return total

def main():
    t = INT()
    for _ in range(t):
        output(f"{solve()}\n")

if __name__ == '__main__':
    main()
