# Problem: B. Ehab Is an Odd Person - https://codeforces.com/problemset/problem/1174/B

n = int(input())
array=list(map(int,input().split()))
a=[0,0]
for i in range(n):
    if array[i] != '0': 
        a[int(array[i])%2] = 1
if all(a):
    array.sort()
print(*array)