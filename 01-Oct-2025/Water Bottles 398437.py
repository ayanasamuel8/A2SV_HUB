# Problem: Water Bottles - https://leetcode.com/problems/water-bottles/description

class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        total_taken = 0
        left = 0
        while numBottles + left >= numExchange:
            total_taken += numBottles
            numBottles += left
            left = numBottles % numExchange
            numBottles //= numExchange
        return total_taken + numBottles