# Problem: E - Strange Mirroring - https://codeforces.com/gym/596141/problem/E

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



def solve():
    string = LINE()
    n = len(string)
    q = INT()
    queries = LIST()

    result = []


    def findCharacter(idx):
        if idx <= n:
            return string[idx - 1]
        
        operation = math.ceil(math.log2(math.ceil(idx/n)))

        idx =idx -  int(pow(2,operation - 1)) * n

        return findCharacter(idx).swapcase()

    for query in queries:
        result.append(findCharacter(query))

    return ' '.join(result)

def main():
    t = INT()
    for _ in range(t):
        output(f"{solve()}\n")

if __name__ == '__main__':

    main()