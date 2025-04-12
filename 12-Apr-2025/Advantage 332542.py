# Problem: Advantage - https://codeforces.com/gym/452236/problem/B

def solve():
    n=int(input())
    s=list(map(int, input().split()))

    arranged = sorted(s)
    maximum = arranged[-1]
    second_max = arranged[-2]

    final = []
    for i in range(len(s)):
        if s[i]==maximum:
            final.append(s[i]-second_max)
        else:
            final.append(s[i]-maximum)
    print(*final)
    
t = int(input())
for _ in range(t):
    solve()