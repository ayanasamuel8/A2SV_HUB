# Problem: F - The Triumphant Empress - https://codeforces.com/gym/601269/problem/F

import sys
from bisect import bisect_left

input = sys.stdin.readline
output = sys.stdout.write

INT = lambda: int(input().strip())
LIST = lambda: list(map(int, input().split()))
LINE = lambda: input().strip()
MATRIX = lambda n, m: [list(map(int, input().split())) for _ in range(n)]

class BIT:
    def __init__(self, size):
        self.n = size + 2 
        self.tree = [0] * self.n
    
    def update(self, index, value=1):
        index += 1 
        while index < self.n:
            self.tree[index] += value
            index += index & -index
    
    def query(self, index):
        index += 1 
        result = 0
        while index > 0:
            result += self.tree[index]
            index -= index & -index
        return result

def compress(values):
    sorted_unique = sorted(set(values))
    return {val: idx for idx, val in enumerate(sorted_unique)}, sorted_unique

def solve():
    n, q = LIST()
    nums = LIST()
    queries = []

    for i in range(q):
        queries.append((LIST(), i))
    
    value_to_index, sorted_value = compress(nums)
    bit = BIT(len(sorted_value))
    queries.sort()
    
    
    results = ['0'] * q
    ptr = 0
    
    for (i, strength), original_idx in queries:
        while ptr < i:
            compressed_idx = value_to_index[nums[ptr]]
            bit.update(compressed_idx)
            ptr += 1
        
        idx = bisect_left(sorted_value, strength) - 1
        count = bit.query(idx) if idx >= 0 else 0
        results[original_idx] = str(count)
    
    output('\n'.join(results) + '\n')

def main():
    T = INT()
    for _ in range(T):
        solve()

if __name__ == "__main__":
    main()