# Problem: Karen and Coffee - https://codeforces.com/contest/816/problem/B

import sys
n,k,q= map(int,sys.stdin.readline().split())

data = sys.stdin.read().splitlines()

recipes = [list(map(int,data[line].split())) for line in range(n)]
questions = [list(map(int, data[line].split())) for line in range(n,n+q)]

prefix_sum = [0] * (int(2*1e5)+2)

def solve():
    
    for i,j in recipes:
        prefix_sum[i] += 1
        prefix_sum[j + 1] -= 1

    for i in range(1,len(prefix_sum)):
        prefix_sum[i] += prefix_sum[i-1]

    prefix_sum[0] = int(prefix_sum[0] >= k)

    for i in range(1,len(prefix_sum)):
        prefix_sum[i] = int(prefix_sum[i] >= k) + prefix_sum[i - 1]

def main():

    solve()

    for i,j in questions:
        print(prefix_sum[j] - prefix_sum[i-1])

if __name__ == '__main__':
    main()