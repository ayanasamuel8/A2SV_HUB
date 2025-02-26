# Problem: G - Evenly Spaced Letters - https://codeforces.com/gym/589822/problem/G

import sys, math
from functools import cmp_to_key
from collections import Counter, defaultdict

input = sys.stdin.readline
output = sys.stdout.write

INT = lambda: int(input().strip())
INTS = lambda: list(map(int, input().split()))
LIST = lambda: list(map(int, input().split()))
LINE = lambda: input().strip()
MATRIX = lambda n, m: [list(map(int, input().split())) for _ in range(n)]

def solve():
    string = LINE()
    counter = [0] * 26

    for i in string:
        counter[ord(i) - ord('a')] += 1
    
    ans =[]
    count = 0

    while len(ans) < len(string):
        for i in range(26):
            if count <= 1 and counter[i] == 2:
                ans.append(chr(i + 97))
            elif count > 1 and counter[i] == 1:
                ans.append(chr(i + 97))
                counter[i] -= 1
        count += 1
    
    output(''.join(ans) + '\n')
    

def main():
    t = INT()
    for _ in range(t):
        solve()

if __name__ == '__main__':
    main()
