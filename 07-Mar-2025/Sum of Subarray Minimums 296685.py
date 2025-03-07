# Problem: Sum of Subarray Minimums - https://leetcode.com/problems/sum-of-subarray-minimums/

class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        total = 0
        n = len(arr)
        stack = []
        MOD = int(1e9 + 7)
        
        for i in range(n):
            while stack and arr[stack[-1]] > arr[i]:
                index = stack.pop()
                left = index - stack[-1] - 1 if stack else index
                right = i - index - 1
                total += arr[index] * (left + 1) * (right + 1)
                total %= MOD
            stack.append(i)
        
        while stack:
            index = stack.pop()
            left = index - stack[-1] - 1 if stack else index
            right = n - index - 1
            total += arr[index] * (left + 1) * (right + 1)
            total %= MOD
        
        return total