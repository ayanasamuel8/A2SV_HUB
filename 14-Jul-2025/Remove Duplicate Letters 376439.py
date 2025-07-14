# Problem: Remove Duplicate Letters - https://leetcode.com/problems/remove-duplicate-letters/

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        cntr = Counter(s)
        stack = []
        seen = set()
        
        for i in s:
            while stack and i not in seen and stack[-1] >= i and cntr[stack[-1]] > 0:
                seen.remove(stack.pop())

            if i not in seen:
                stack.append(i)
                seen.add(i)
            cntr[i] -= 1
        
        return ''.join(stack)