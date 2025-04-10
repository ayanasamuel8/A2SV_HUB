# Problem: Merge Sort - https://codeforces.com/problemset/problem/873/D

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

def mergeSort(nums, m):
    global count
    if count >= m or len(nums) == 1:
        return nums
    count += 2
    mid = math.ceil(len(nums) / 2)
    left = mergeSort(nums[:mid],m)
    right = mergeSort(nums[mid:],m)
    return right + left
    

def solve():
    # n = INT()
    global count
    count = 1
    
    n, m = LIST()    
    nums = [i + 1 for i in range(n)]
    ans = mergeSort(nums,m)

    if count != m:
        return [-1]
    else:
        return ans

def main():
    T = 1
    # T = INT()
    for _ in range(T):
        output(f"{' '.join(map(str,solve()))}")

if __name__ == '__main__':
    main()
