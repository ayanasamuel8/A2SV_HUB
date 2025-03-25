# Problem: Capacity To Ship Packages Within D Days - https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/

class Solution:
    def canShipWithWeight(self, weight, weights, days):
        total = 0
        count = 1
        for i in range(len(weights)):
            total += weights[i]
            if total > weight:
                count += 1
                total = weights[i]
        return count <= days


    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left, right = max(weights), sum(weights)

        while left <= right:
            mid = left + (right - left) // 2

            if self.canShipWithWeight(mid, weights, days):
                right = mid - 1
            else:
                left = mid + 1
        return left