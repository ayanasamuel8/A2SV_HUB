# Problem: Put Marbles in Bags - https://leetcode.com/problems/put-marbles-in-bags/

class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        n = len(weights)
        if k == n:
            return 0
        split_ = []
        for i in range(n - 1):
            split_.append(weights[i] + weights[i + 1])
        split_.sort()
        left = split_[-k:]
        right = split_[:k]
        print(left, right)

        return sum(left[1:]) - sum(right[:-1])