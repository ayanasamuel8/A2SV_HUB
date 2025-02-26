# Problem: C - Binary Flip - https://codeforces.com/gym/590053/problem/C

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


def solve():
    n = INT()
    string = LINE()
    string2 = LINE()

    prefix = [0,0]
    for i in string:
        prefix[int(i)] += 1
    
    flipped = False

    for i in range(n - 1, -1, -1):
        if not flipped and string[i] != string2[i]:
            if prefix[0] != prefix[1]:
                return False
            flipped = True
        if flipped and string[i ] == string2[i]:
            if prefix[0] != prefix[1]:
                return False
            flipped = False
        if not flipped:
            prefix[int(string[i])] -= 1
        else:
            prefix[1- int(string[i])] -= 1
    return True

def main():
    T = INT()
    for _ in range(T):
        if solve():
            print('YES')
        else:
            print('NO')

if __name__ == '__main__':
    main()
