# Problem: E - Symmetrization - https://codeforces.com/gym/586960/problem/E

t = int(input())
while t:
    t-=1
    n=int(input())
    matrix=[]
    for i in range(n):
        matrix.append([])
        for j in input():
            matrix[-1].append(int(j))
    different=0
    for i in range(n):
        for j in range(n):
            arr=[0,0]
            arr[matrix[i][j]]+=1
            arr[matrix[n-j-1][i]]+=1
            arr[matrix[n-i-1][n-j-1]]+=1
            arr[matrix[j][n-i-1]]+=1
            different+=min(arr)
    print(different//4)