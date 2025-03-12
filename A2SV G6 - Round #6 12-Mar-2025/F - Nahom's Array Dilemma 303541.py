# Problem: F - Nahom's Array Dilemma - https://codeforces.com/gym/594077/problem/F

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

def check(array, prefix, n):
    mono_stack = []
    for i in range(n):
        while mono_stack and mono_stack[-1][0] <= array[i]:
            if prefix[i] - prefix[mono_stack[-1][1]] > 0:
                return False
            mono_stack.pop()

        mono_stack.append([array[i], i])
    return True


def solve():
    n = INT()
    nums = LIST()
    reversed_num = list(reversed(nums))
    prefix = [0]
    rev_prefix = [0]
    for i in range(n):
        prefix.append(prefix[-1] + nums[i])
        rev_prefix.append(rev_prefix[-1] + reversed_num[i])
    
    return check(nums, prefix, n) and check(reversed_num, rev_prefix, n)
    

def main():
    t = INT()
    for _ in range(t):
        if solve():
            output('YES\n')
        else:
            output('NO\n')

if __name__ == '__main__':
    main()
