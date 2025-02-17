# Problem: Maximum subarray - https://leetcode.com/problems/maximum-subarray/

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        min_sum = float('inf')
        running_sum = 0
        max_sum = float('-inf')
        
        for i in nums:
            running_sum += i
            max_sum = max(running_sum,max_sum,running_sum - min_sum)
            min_sum = min(min_sum,running_sum)
        return max_sum