# Problem: Kuriyama Mirai's Stones - https://codeforces.com/contest/433/problem/B

import sys, math
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
    n = INT()
    nums = LIST()

    sorted_nums = sorted(nums)
    nums = prefixSum(nums, n)
    sorted_nums = prefixSum(sorted_nums, n)

    q = INT()
    queries = MATRIX(q, 3)

    for type, left, right in queries:
        if type == 1:
            output(f"{nums[right] - nums[left - 1]}\n")
        else:
            output(f"{sorted_nums[right] - sorted_nums[left - 1]}\n")
    

def main():
    solve()

if __name__ == '__main__':
    main()
