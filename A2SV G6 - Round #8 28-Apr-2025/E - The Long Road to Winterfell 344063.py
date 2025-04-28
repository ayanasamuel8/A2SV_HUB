# Problem: E - The Long Road to Winterfell - https://codeforces.com/gym/599383/problem/E

import sys
from bisect import bisect_left, bisect_right

input = sys.stdin.readline
output = sys.stdout.write

INT = lambda: int(input().strip())
LIST = lambda: list(map(int, input().split()))
LINE = lambda: input().strip()

def solve():
    n, k = LIST()
    rooms = LINE()
    zeros = []
    for i in range(n):
        if rooms[i] == '0':
            zeros.append(i)
    
    distance = float('inf')
    left = 0
    
    for right in range(k, len(zeros)):
        mid = (zeros[left] + zeros[right]) // 2
        
        r = bisect_left(zeros, mid)
        
        for candidate in [r, r-1]:
            if left <= candidate <= right:
                current_dist = max(zeros[candidate] - zeros[left], zeros[right] - zeros[candidate])
                distance = min(distance, current_dist)
        
        left += 1

    print(distance)

def main():
    T = 1
    # T = INT()
    for _ in range(T):
        solve()

if __name__ == '__main__':
    main()