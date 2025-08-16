# Problem: Print Words Vertically - https://leetcode.com/problems/print-words-vertically/description/

class Solution:
    def printVertically(self, s: str) -> List[str]:
        lst = s.split()
        max_len = max(len(i) for i in lst)
        n = len(lst)
        ans = []
        for i in range(max_len):
            curr = []
            for j in range(n):
                curr.append(lst[j][i] if i < len(lst[j]) else ' ')
            ans.append(''.join(curr).rstrip())
        
        return ans