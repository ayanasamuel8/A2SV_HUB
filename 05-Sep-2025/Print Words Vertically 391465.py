# Problem: Print Words Vertically - https://leetcode.com/problems/print-words-vertically/description/

class Solution:
    def printVertically(self, s: str) -> List[str]:
        words = s.split()
        
        _max = max(len(word) for word in words)
        
        ans = []
        
        for i in range(_max):
            cur_row = []
            for word in words:
                if i < len(word):
                    cur_row.append(word[i])
                else:
                    cur_row.append(" ")
            ans.append("".join(cur_row).rstrip())
        
        return ans
