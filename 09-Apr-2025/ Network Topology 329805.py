# Problem:  Network Topology - https://codeforces.com/problemset/problem/292/B

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

def isBus(indegree):
    one = 0
    for i in indegree:
        if i == 1 and one < 2:
            one += 1
        elif i == 2:
            continue
        else:
            return False
    return True

def isRing(indegree):
    set_indeg = set(indegree)
    return len(set_indeg) == 1 and {2} == set_indeg

def isStar(indegree, m):
    set_indeg = set(indegree)
    return {m,1} == set_indeg
        
def solve():
    n, m = LIST()

    edges = MATRIX(m, 2)
    indegree = [0] * (n + 1)

    for start, end in edges:
        indegree[end] += 1
        indegree[start] += 1
    
    indegree = indegree[1:]

    if m == n:
        return "ring topology" if isRing(indegree) else "unknown topology"
    elif m == n - 1:
        if isBus(indegree):
            return "bus topology"
        elif isStar(indegree, m):
            return "star topology"
        else:
            return "unknown topology"
    else:
        return "unknown topology"
    
        
    

def main():
    T = 1
    # T = INT()
    for _ in range(T):
        output(f"{solve()}\n")

if __name__ == '__main__':
    main()
