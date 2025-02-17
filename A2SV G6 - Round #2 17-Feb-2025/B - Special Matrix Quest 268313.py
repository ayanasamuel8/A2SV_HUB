# Problem: B - Special Matrix Quest - https://codeforces.com/gym/586960/problem/B

n = int(input())
matrix=[]
for i in range(n):
    matrix.append(list(map(int,input().split())))
max_sum=0
half=n//2
for i in range(n):
    max_sum+=matrix[i][i]
    max_sum+=matrix[i][n-i-1]
    max_sum+=matrix[i][half]
    max_sum+=matrix[half][i]
print(max_sum-matrix[half][half]*3)