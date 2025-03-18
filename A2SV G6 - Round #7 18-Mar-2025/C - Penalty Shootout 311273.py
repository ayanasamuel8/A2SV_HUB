# Problem: C - Penalty Shootout - https://codeforces.com/gym/596141/problem/C

import sys, math, threading
from collections import Counter, defaultdict,deque
from functools import cmp_to_key

input = sys.stdin.readline
output = sys.stdout.write

INT = lambda: int(input().strip())
INTS = lambda: list(map(int, input().split()))
LIST = lambda: list(map(int, input().split()))
LINE = lambda: input().strip()
MATRIX = lambda n, m: [list(map(int, input().split())) for _ in range(n)]

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def solve():
    string = LINE()
    n = len(string)
    firstWin = []
    secondWin = []
    for i in range(n):
        if i % 2 == 0:
            firstWin.append(0 if string[i] == '0' else 1)
            secondWin.append(1 if string[i] == '1' else 0)
        else:
            firstWin.append(1 if string[i] == '1' else 0)
            secondWin.append(0 if string[i] == '0' else 1)

    def minTime(curr):
        first = 0
        second = 0
        length = len(curr)
        for i in range(length):
            if i % 2 == 0:
                first += curr[i]
                if second - first > (length - i - 1) // 2:
                    return i + 1
            else:
                second += curr[i]
                if first - second > (length - i - 1) // 2:
                    return i + 1
            if abs(first - second) > (length - i) // 2:
                return i + 1
        return length
    return(min(minTime(firstWin), minTime(secondWin)))
    
def main():
    t = INT()
    for _ in range(t):
        output(f"{solve()}\n")

if __name__ == '__main__':

    main()
