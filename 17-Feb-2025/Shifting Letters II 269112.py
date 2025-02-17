# Problem: Shifting Letters II - https://leetcode.com/problems/shifting-letters-ii/

class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        prefix_sum = [0]*(len(s)+1)
        for i,j,d in shifts:
            prefix_sum[i] += (d==1)
            prefix_sum[i] -= (d==0)
            prefix_sum[j+1] -= (d==1)
            prefix_sum[j+1] += (d==0)
        for i in range(1,len(prefix_sum)):
            prefix_sum[i]+=prefix_sum[i-1]
        ans=[]
        for  i in range(len(s)):
            shift = (ord(s[i]) + prefix_sum[i]%26)
            if shift < 97: 
                shift += 26
                ans.append(chr(shift))
            elif shift > 122: ans.append(chr(97 + shift % 123))
            else: ans.append(chr(shift))
            
        return ''.join(ans)