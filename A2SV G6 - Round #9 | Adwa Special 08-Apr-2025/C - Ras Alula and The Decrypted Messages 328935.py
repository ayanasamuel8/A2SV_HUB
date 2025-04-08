# Problem: C - Ras Alula and The Decrypted Messages - https://codeforces.com/gym/601269/problem/C

import sys, math
from collections import Counter, defaultdict,deque
from functools import cmp_to_key
from bisect import bisect_left, bisect_right,insort

input = sys.stdin.readline
output = sys.stdout.write

INT = lambda: int(input().strip())
LIST = lambda: list(map(int, input().split()))
LINE = lambda: input().strip()
MATRIX = lambda n, m: [list(map(int, input().split())) for _ in range(n)]


def solve():
    n, m = LIST()
    string1 = LINE()
    string2 = LINE()
    if n < m: return False

    total = 0
    running_sum = 0
    for i in range(m):
        total += ord(string2[i])
        running_sum += ord(string1[i])
    if running_sum == total: 
        return True
    for i in range(m, n):
        running_sum -= ord(string1[i - m])
        running_sum += ord(string1[i])
        if running_sum == total:
            return True
    return False
    

        
    

def main():
    T = 1
    T = INT()
    for _ in range(T):
        if solve():
            output('YES\n')
        else:
            output('NO\n')

if __name__ == '__main__':
    main()
