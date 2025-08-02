# Problem: Minimum Add To Make Parentheses Valid - https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/

class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        open_ = 0
        count = 0
        for i in s:
            if i == ')':
                if open_:
                    open_ -= 1
                else:
                    count += 1
                continue
            open_ += 1
        
        return count + open_