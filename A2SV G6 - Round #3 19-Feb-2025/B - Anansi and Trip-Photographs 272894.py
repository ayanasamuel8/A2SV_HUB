# Problem: B - Anansi and Trip-Photographs - https://codeforces.com/gym/588468/problem/B

t = int(input())
while t:
    t -= 1
    n,k = map(int,input().split())
    array = list(map(int,input().split()))
    array.sort()
    for i in range(n):
        if array[i+n]-array[i]<k:
            print('NO')
            break
    else:
        print('YES')