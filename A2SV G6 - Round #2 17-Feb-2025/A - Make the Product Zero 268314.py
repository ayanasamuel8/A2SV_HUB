# Problem: A - Make the Product Zero - https://codeforces.com/gym/586960/problem/A

n = int(input())
array=list(map(int,input().split()))
minel=float('inf')
for i in range(n):
    minel=min(minel,abs(array[i]))
print(minel)