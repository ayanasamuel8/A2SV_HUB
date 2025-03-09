# Problem: Segments with Small Spread - https://codeforces.com/edu/course/2/lesson/9/2/practice/contest/307093/problem/F

import sys
from collections import deque
n,m,*array = map(int,sys.stdin.read().split())
min_el,max_el=float('inf'),float('-inf')
left=right=0
ans = 0
min_deque = deque()
max_deque = deque()
for right in range(n):
    while min_deque and min_deque[-1]>array[right]:
        min_deque.pop()
    while max_deque and max_deque[-1]<array[right]:
        max_deque.pop()
    min_deque.append(array[right])
    max_deque.append(array[right])
    while max_deque[0] -min_deque[0]>m:
        ans+=right-left
        if max_deque[0]==array[left]:
            max_deque.popleft()
        if min_deque[0]==array[left]:
            min_deque.popleft()
        left+=1
ans+=((right-left+1)*(right-left+2)//2)
print(ans)