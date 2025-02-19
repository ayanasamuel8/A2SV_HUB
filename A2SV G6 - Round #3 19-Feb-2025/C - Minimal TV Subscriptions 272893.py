# Problem: C - Minimal TV Subscriptions - https://codeforces.com/gym/588468/problem/C

from collections import defaultdict, Counter
t = int(input())
while t:
    t -= 1
    n,k,d = map(int,input().split())
    array = list(map(int,input().split()))
    uniques = defaultdict(int)
    for i in range(d):
        uniques[array[i]] += 1
    ans = len(uniques)
    for i in range(d,n):
        uniques[array[i-d]] -= 1
        uniques[array[i]] += 1
        if uniques[array[i-d]] == 0:
            del uniques[array[i-d]]
        ans = min(ans,len(uniques))
    print(ans)