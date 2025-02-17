# Problem: D - Repeating Cipher - https://codeforces.com/gym/585107/problem/D

n=int(input())
s=input()
i=0
add=1
ans=''
while i<n:
    j=i+1
    for j in range(i+1,min(i+add,n)):
        if s[j]!=s[i]:
            break
    ans+=s[i]
    add+=1
    i=j+1
print(ans)