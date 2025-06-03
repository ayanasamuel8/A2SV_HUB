# Problem: Maximum Points You Can Obtain from Cards - https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/

class Solution:
    def minSubarray(self, nums, size):
        count = 0
        for i in range(size):
            count += nums[i]
        min_sum = count
        for i in range(size, len(nums)):
            count -= nums[i - size]
            count += nums[i]
            min_sum = min(min_sum, count)
        return min_sum

    def maxScore(self, cardPoints: List[int], k: int) -> int:
        size = (n:= len(cardPoints)) - k
        return sum(cardPoints) - self.minSubarray(cardPoints, size)