# Problem: Subarray Sum Equals K - https://leetcode.com/problems/subarray-sum-equals-k/

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        running_sum = 0
        prefix_sum = defaultdict(int)
        prefix_sum[0] = 1

        total_subarray = 0

        for num in nums:
            running_sum += num
            total_subarray += prefix_sum[running_sum - k]
            prefix_sum[running_sum] += 1
        
        return total_subarray
        