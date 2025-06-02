# Problem: Candy - https://leetcode.com/problems/candy/

class Solution:
    def candy(self, ratings: List[int]) -> int:
        candies_allocated = [0] * (n:=len(ratings))
        candies_allocated[0] = 1
        for i in range(1, n):
            candies_allocated[i] = 1
            if ratings[i] < ratings[i - 1] and candies_allocated[i -1] <= candies_allocated[i]:
                candies_allocated[i - 1] = candies_allocated[i] + 1
            elif ratings[i] > ratings[i - 1]:
                candies_allocated[i] = candies_allocated[i - 1] + 1
        candies_allocated2 = [0] * n
        candies_allocated2[n -1] = 1
        for i in range(n - 2, -1, -1):
            candies_allocated2[i] = 1
            if ratings[i] < ratings[i + 1] and candies_allocated2[i + 1] <= candies_allocated2[i]:
                candies_allocated2[i + 1] = candies_allocated2[i] + 1
            elif ratings[i] > ratings[i + 1]:
                candies_allocated2[i] = candies_allocated2[i + 1] + 1
        ans = 0
        for i in range(n):
            ans += max(candies_allocated[i], candies_allocated2[i])
        return ans