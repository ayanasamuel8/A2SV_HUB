# Problem: Limited Repainting - https://codeforces.com/contest/2070/problem/C

import sys, math
from collections import Counter, defaultdict,deque
from functools import cmp_to_key
from bisect import bisect_left, bisect_right

input = sys.stdin.readline
output = sys.stdout.write

INT = lambda: int(input().strip())
LIST = lambda: list(map(int, input().split()))
LINE = lambda: input().strip()
MATRIX = lambda n, m: [list(map(int, input().split())) for _ in range(n)]

def solve():
    n, k = LIST()

    string = LINE()
    nums = LIST()

    def isPosible(penality):
        operations = 0
        i = 0

        while i < n:
            if string[i] == 'B' and nums[i] > penality:
                operations += 1
                if operations > k:
                    return False

                j = i
                while j < n and (string[j] == 'B' or nums[j] <= penality):
                    j += 1
                i = j
            else:
                i += 1
        return operations <= k
    
    left, right = 0, sum(nums)
    while left <= right:
        mid = left + (right - left) // 2

        if isPosible(mid):
            right = mid - 1
        else:
            left = mid + 1
    return left

        



def main():
    T = INT()
    for _ in range(T):
        output(f"{solve()}\n")

if __name__ == '__main__':
    main()
