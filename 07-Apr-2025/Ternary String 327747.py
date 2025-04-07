# Problem: Ternary String - https://codeforces.com/gym/455166/problem/D

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
    string = LINE()
    n = len(string)

    hashmap = defaultdict(int)
    needed = Counter(['1','2','3'])
    left = 0
    ans = float('inf')
    for right in range(n):
        if string[right] in needed:
            hashmap[string[right]] += 1
        while len(hashmap) == 3:
            ans = min(ans, right - left + 1)
            if string[left] in needed:
                hashmap[string[left]] -= 1
                if hashmap[string[left]] == 0:
                    del hashmap[string[left]]
            left += 1
    output(f"{ans if ans != float('inf') else 0}\n")

def main():
    T = INT()
    for _ in range(T):
        solve()

if __name__ == '__main__':
    main()
