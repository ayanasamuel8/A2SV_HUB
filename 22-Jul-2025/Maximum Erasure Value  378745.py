# Problem: Maximum Erasure Value  - https://leetcode.com/problems/maximum-erasure-value/

class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        curr_sum = 0
        score = 0
        freq = defaultdict(int)
        n = len(nums)
        left = 0

        for i in range(n):
            while freq[nums[i]] >= 1:
                freq[nums[left]] -= 1
                curr_sum -= nums[left]
                left += 1
            curr_sum += nums[i]
            freq[nums[i]] += 1
            score = max(score, curr_sum)

        return score