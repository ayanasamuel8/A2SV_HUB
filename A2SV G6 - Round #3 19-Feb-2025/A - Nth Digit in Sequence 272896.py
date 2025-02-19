# Problem: A - Nth Digit in Sequence - https://codeforces.com/gym/588468/problem/A

n = int(input())
s=''.join(map(str,list(range(1,n+1))))
print(s[n-1])