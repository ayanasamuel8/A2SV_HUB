# Problem: Belted Rooms - https://codeforces.com/problemset/problem/1428/B

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
    n = INT()
    # n, m = LIST()
    # nums = LIST()
    string = LINE()
    if '<' not in string or '>' not in string:
        return n
    
    cycles = [0] * n
    for i in range(n):
        if string[i] == '-':
            v =  (i + 1) % n
            cycles[i] = 1
            cycles[v] = 1
    
    return sum(cycles)
    
    
    
    

def main():
    T = 1
    T = INT()
    for _ in range(T):
        output(f"{solve()}\n")

if __name__ == '__main__':
    main()
