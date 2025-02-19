# Problem: F - Binary Substrings with Exactly k Ones - https://codeforces.com/gym/588468/problem/F

k = int(input())
s = input()
def count(l):
    if l<0: return 0
    ones_count = left = 0
    ans = 0
    for right in range(len(s)):
        ones_count += int(s[right])
        while ones_count > l:
            ans += right - left
            ones_count -= int(s[left])
            left += 1
    while left<len(s):
        ans += len(s) - left
        ones_count -= int(s[left])
        left += 1
    return ans 
print(count(k)-count(k-1))