# Problem: B - Square String? - https://codeforces.com/gym/585107/problem/B

t=int(input())
while t:
    t-=1
    s=input()
    for i in range(len(s)+1):
        if s[:i]==s[i:]:
            print("YES")
            break
    else: print("NO")