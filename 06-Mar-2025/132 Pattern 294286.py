# Problem: 132 Pattern - https://leetcode.com/problems/132-pattern/

class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []
        front = float('-inf')
        for i in nums[::-1]:
            if front > i: return True
            while stack and stack[-1] < i:
                front = stack[-1]
                stack.pop()
            stack.append(i)
        return False