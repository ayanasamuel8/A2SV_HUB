# Problem: E - Minimum Subsequence - https://codeforces.com/gym/594077/problem/E

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
    string = LINE()
    count = 0
    stack0 = []
    stack1 = []
    result = []

    for i in string:
        if i == '0':
            if stack1:
                result.append(stack1[-1])
                stack0.append(stack1.pop())
            else:
                count += 1
                result.append(count)
                stack0.append(count)
        else:
            if stack0:
                result.append(stack0[-1])
                stack1.append(stack0.pop())
            else:
                count += 1
                result.append(count)
                stack1.append(count)
    output(f"{max(result)}\n")
    return ' '.join(map(str,result))

def main():
    t = INT()
    for _ in range(t):
        output(f"{solve()}\n")

if __name__ == '__main__':
    main()
