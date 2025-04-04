# Problem: Masha and a Beautiful Tree - https://codeforces.com/problemset/problem/1741/D

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

def divide(left,right, nums):
    global count
    if right - left == 1:
        sortedSubtree = sorted(nums[left: right + 1])
        if sortedSubtree != nums[left: right + 1]:
            count += 1
        nums[left: right + 1] = sortedSubtree
        return True
    mid = (left + right) // 2
    if not divide(left, mid, nums):
        return False
    left_num = nums[left : mid + 1]
    if not divide(mid + 1,right, nums):
        return False
    right_num = nums[mid + 1: right + 1]
    ret,val = checkIfSorted(left_num, right_num)
    nums[left:right + 1] = val

    return ret

def checkIfSorted(left, right):
    global count
    sortedSubtree = sorted(left + right)
    if left + right == sortedSubtree:
        return True, sortedSubtree
    elif right + left == sortedSubtree:
        count += 1
        return True,sortedSubtree
    return False,sortedSubtree

def solve():
    global count
    count = 0
    n = INT()
    nums = LIST()
    if n < 2:
        return 0
    if not divide(0, n - 1, nums):
        return -1
    else:
        return count
    

def main():
    global count
    T = INT()
    for _ in range(T):
        output(f"{solve()}\n")

if __name__ == '__main__':
    main()
