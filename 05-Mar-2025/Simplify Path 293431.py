# Problem: Simplify Path - https://leetcode.com/problems/simplify-path/

class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split('/')
        stack = []
        for i in path:
            if i and i != '.' and i != '..':
                stack.append(i)
            elif i == '..' and stack: 
                stack.pop()
        return '/' + '/'.join(stack)