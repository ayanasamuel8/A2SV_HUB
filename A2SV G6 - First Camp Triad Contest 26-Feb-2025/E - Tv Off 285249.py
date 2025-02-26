# Problem: E - Tv Off - https://codeforces.com/gym/589822/problem/E

import sys
from math import gcd
from functools import cmp_to_key
from collections import Counter, defaultdict

input = sys.stdin.readline
output = sys.stdout.write

INT = lambda: int(input().strip())
INTS = lambda: list(map(int, input().split()))
LIST = lambda: list(map(int, input().split()))
LINE = lambda: input().strip()
MATRIX = lambda n, m: [list(map(int, input().split())) for _ in range(n)]
def COMPARATOR(a, b):
    if a[0] < b[0]:
        return -1
    elif a[0] > b[0]:
        return 1
    elif a[1] > b[1]:
        return -1
    else:
        return 1

def prefixSum(array, n):
    prefix_sum = [0]*(n + 1)

    for i in range(n):
        prefix_sum[i + 1] = prefix_sum[i] + array[i]

    return prefix_sum

def solve():
    n = INT()
    sockets = MATRIX(n, 2)
    hashmap = {tuple(socket): indx + 1 for indx, socket in enumerate(sockets)}
    sockets.sort(key = cmp_to_key(COMPARATOR))
    
    ans = -1
    for i in range(1,n - 1):
        if sockets[i][1] <= sockets[i - 1][1] or sockets[i - 1][1] >= sockets[i + 1][0] - 1:
            ans = hashmap[tuple(sockets[i])]
    if n > 1 and sockets[n - 1][1] <= sockets[n - 2][1]: 
        ans = hashmap[tuple(sockets[n - 1])]
    
    print(ans)
    

def main():
    solve()

if __name__ == '__main__':
    main()
