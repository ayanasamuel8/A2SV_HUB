# Problem: Christmas Spruce - https://codeforces.com/contest/913/problem/B

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


def solve():
    n = INT()
    is_leaf = [True] * n
    childrens = [[] for _ in range(n)]

    for i in range(1,n):
        curr = INT()
        curr -= 1
        childrens[curr].append(i)
        is_leaf[curr] = False

    for children in childrens:
        if children:
            cnt = 0
            for i in children:
                if is_leaf[i]:
                    cnt += 1
            if cnt < 3:
                output('No\n')
                break
    else:
        output('Yes\n')

def main():
    solve()

if __name__ == '__main__':
    main()
