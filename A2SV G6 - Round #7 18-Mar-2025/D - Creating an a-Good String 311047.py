# Problem: D - Creating an a-Good String - https://codeforces.com/gym/596141/problem/D

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
    h = INT()
    string = LINE()
    alphas = 'abcdefghijklmnopqrstuvwxyz'
    def recursion(input, index):
        n = len(input)
        curr = alphas[index % 26]
        if n == 1:
            return 0 if input[0] == curr else 1

        str1 = input[:n//2]
        str2= input[n//2:]
        
        left = n//2 - str1.count(curr)
        right = n//2 - str2.count(curr)
        from_left = recursion(str2, index + 1)
        from_right = recursion(str1, index + 1)
        return min(left + from_left, right + from_right)
    output(f"{recursion(string, 0)}\n")


def main():
    T = INT()
    for _ in range(T):
        solve()

if __name__ == '__main__':
    main()
