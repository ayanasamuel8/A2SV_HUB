# Problem: Maximize Happiness of Selected Children - https://leetcode.com/problems/maximize-happiness-of-selected-children/?envType=daily-question&envId=2024-05-09

class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        total = 0
        happiness = sorted(happiness)
        n = len(happiness)
        decrement = 0
        count = 0

        for i in range(n - 1, max(-1, n - k - 1), -1):

            if happiness[i] - decrement <= 0: 
                break
            count += happiness[i] - decrement
            decrement += 1

        return count
