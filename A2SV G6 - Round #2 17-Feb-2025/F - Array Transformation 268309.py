# Problem: F - Array Transformation - https://codeforces.com/gym/586960/problem/F

from collections import defaultdict,Counter
t = int(input())
while t:
    t-=1
    n=int(input())
    array=list(map(int,input().split()))
    freq_count=Counter(array)
    sor=[]
    for key,value in freq_count.items():
        sor.append(value)
    sor.sort(reverse=True)
    pushed=sor[0]
    cnt=1
    ans=sor[0]
    for i in range(1,len(sor)):
        if sor[i] <sor[i-1]:
            pushed-=((sor[i-1]-sor[i])*cnt)
            pushed+=sor[i]
        else:
            pushed+=sor[i]
        ans=max(ans,pushed)
        cnt+=1
    print(n-ans)
