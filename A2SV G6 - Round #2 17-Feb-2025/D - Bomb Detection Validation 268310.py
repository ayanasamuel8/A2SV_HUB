# Problem: D - Bomb Detection Validation - https://codeforces.com/gym/586960/problem/D

n,m=map(int,input().split())
game=[]
for i in range(n):
    game.append([])
    for j in input():
        game[-1].append(j)
for i in range(n):
    for j in range(m):
        if game[i][j].isdigit():
            game[i][j]=int(game[i][j])

drxn=[[1,0],[0,1],[1,-1],[-1,1],[1,1],[-1,0],[0,-1],[-1,-1],[0,0]]
def valid(x,y):
    return x>=0 and y>=0 and x<n and y<m
def count_num(x,y):
    cnt=0
    for i,j in drxn:
        if valid(x+i,y+j) and game[x+i][y+j]=='*':
            cnt+=1
    return cnt
for i in range(n):
    for j in range(m):
        if game[i][j]=='*':
            for x,y in drxn:
                if valid(i+x,j+y) and game[i+x][j+y]=='.':
                    print('NO')
                    break
            else:
                continue
            break
        elif type(game[i][j])==int:
            if game[i][j] != count_num(i,j):
                print('NO')
                break
    else:
        continue
    break
else:
    print('YES')