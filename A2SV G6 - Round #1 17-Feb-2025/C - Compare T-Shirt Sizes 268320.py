# Problem: C - Compare T-Shirt Sizes - https://codeforces.com/gym/585107/problem/C

t=int(input())
while t:
    t-=1
    s1,s2=input().split()
    if (s1[-1]!=s2[-1]):
        if (s1[-1]=='S'):
            print('<')
        elif (s1[-1]=='L'):
            print('>')
        elif (s2[-1]=='S'):
            print('>')
        elif (s2[-1]=='L'):
            print('<')
    else:
        if len(s1)==len(s2):
            print('=')
        else:
            if(s1[-1]=='L'):
                print('>' if len(s1)>len(s2) else '<')
            if(s1[-1]=='S'):
                print('>' if len(s1)<len(s2) else '<')
