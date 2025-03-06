# Problem: F - The Last Problem - https://codeforces.com/gym/591928/problem/F

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

def isValid(x,y,n):
    return x >= 0 and y < n

def solve():
    n = INT()
    nums1 = LIST()
    nums2 = LIST()
    array = []
    for i in range(n):
        array.append(nums1[i] * nums2[i])
    
    array = prefixSum(array, n)
    total = array[-1]
    max_sum = total
    #odd
    for i in range(n - 1):
        left = i - 1
        right = i + 1
        curr_sum = array[i + 1] - array[i]
        while isValid(left,right,n):
            curr_total = total - array[right + 1] + array[left]
            curr_sum += nums1[left] * nums2[right]
            curr_sum += nums2[left] * nums1[right]
            curr_total += curr_sum
            max_sum = max(max_sum, curr_total)
            left -= 1
            right += 1
    
    #Even
    for i in range(n):
        left = i
        right = i + 1
        curr_sum = 0
        while isValid(left,right,n):
            curr_total = total - array[right + 1] + array[left]
            curr_sum += nums1[left] * nums2[right]
            curr_sum += nums2[left] * nums1[right]
            curr_total += curr_sum
            max_sum = max(max_sum, curr_total)
            left -= 1
            right += 1
    return max_sum

def main():
    output(f"{solve()}")

if __name__ == '__main__':
    main()
