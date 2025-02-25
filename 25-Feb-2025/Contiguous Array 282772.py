# Problem: Contiguous Array - https://leetcode.com/problems/contiguous-array/

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        prefix_sum = dict()
        prefix_sum[0] = -1
        running_sum = 0
        n= len(nums)
        max_len = 0

        for right in range(n):
            if nums[right] == 1: running_sum += 1
            else: running_sum -= 1
            
            if running_sum in prefix_sum:
                left = prefix_sum[running_sum]
                max_len = max(max_len, right-left)
            else:
                prefix_sum[running_sum] = right
        
        return max_len