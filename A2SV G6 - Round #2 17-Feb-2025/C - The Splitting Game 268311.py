# Problem: C - The Splitting Game - https://codeforces.com/gym/586960/problem/C

from collections import Counter,defaultdict
t = int(input())
while t:
    t-=1
    n=int(input())
    s=input()
    first=Counter(s)
    second=defaultdict(int)
    max_sum=len(first)
    for i in s:
        first[i]-=1
        if first[i]==0:
            del first[i]
        second[i]+=1
        max_sum=max(max_sum,len(first)+len(second))
    print(max_sum)