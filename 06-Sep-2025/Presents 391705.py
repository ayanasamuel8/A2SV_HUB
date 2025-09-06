# Problem: Presents - https://codeforces.com/problemset/problem/136/A

n=int(input())
array=list(map(int,input().split()))
ans=[-1]*n
for i in range(n):
    ans[array[i]-1]=i+1
print(*ans)