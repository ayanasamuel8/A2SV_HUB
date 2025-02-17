# Problem: Subarray Sums Divisible by K - https://leetcode.com/problems/subarray-sums-divisible-by-k/

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        n = len(nums)
        running_sum = 0
        remainders = defaultdict(int)
        remainders[0] = 1

        total_subarray = 0

        for i in range(n):
            running_sum += nums[i]
            total_subarray += remainders[running_sum % k]
            remainders[running_sum % k] += 1
        
        return total_subarray