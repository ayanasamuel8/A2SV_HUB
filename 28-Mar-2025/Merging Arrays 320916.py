# Problem: Merging Arrays - https://codeforces.com/edu/course/2/lesson/9/1/practice/contest/307092/problem/A

n, m = map(int, input().split())
l1=list(map(int,input().split()))
l2=list(map(int,input().split()))
left=right=0
ans=[]
while left<len(l1) and right<len(l2):
    if(l1[left]<=l2[right]):
        ans.append(l1[left])
        left+=1
    else:
        ans.append(l2[right])
        right+=1
ans.extend(l1[left:])
ans.extend(l2[right:])
for i in ans:
    print(i,end=" ")