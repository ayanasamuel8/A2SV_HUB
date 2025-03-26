# Problem: Skibidus and Fanum Tax (hard version) - http://codeforces.com/problemset/problem/2065/C2

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
    n, m = LIST()
    nums1 = LIST()
    nums2 = LIST()

    nums2.sort()

    if nums1[0] > nums2[0] - nums1[0]:
        nums1[0] = nums2[0] - nums1[0]
    for i in range(1, n):
        diff = nums1[i] + nums1[i - 1]
        left = bisect_left(nums2,diff)
        if nums1[i] >= nums1[i - 1]:
            if left != m:
                nums1[i] = min(nums1[i], nums2[left] - nums1[i])
        elif left == m:
            return False
        else:
            nums1[i] = nums2[left] - nums1[i]
    return True


    

def main():
    T = INT()
    for _ in range(T):
        if solve():
            output("YES\n")
        else:
            output('NO\n')

if __name__ == '__main__':
    main()
