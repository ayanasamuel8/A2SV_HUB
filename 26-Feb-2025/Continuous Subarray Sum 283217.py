# Problem: Continuous Subarray Sum - https://leetcode.com/problems/continuous-subarray-sum/

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        seen = {0:-1}
        running_sum = 0
        total_subarray = 0
        
        for i in range(len(nums)):
            running_sum += nums[i]
            calc = running_sum % k
            if calc in seen and i - seen[calc] > 1:
                return True
            elif calc not in seen: seen[calc] = i
        return False