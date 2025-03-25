# Problem: Koko Eating Bananas - https://leetcode.com/problems/koko-eating-bananas/

class Solution:
    def canEatPile(self, piles, hour, pile):
        time_required = 0
        for i in piles:
            time_required += math.ceil(i / pile)
        return time_required <= hour

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        while left <= right:
            mid = left + (right - left) // 2
            if self.canEatPile(piles, h, mid):
                right = mid - 1
            else:
                left = mid + 1
        return left