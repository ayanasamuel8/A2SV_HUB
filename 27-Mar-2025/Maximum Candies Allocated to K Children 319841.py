# Problem: Maximum Candies Allocated to K Children - https://leetcode.com/problems/maximum-candies-allocated-to-k-children/

class Solution:
    def helper(self, candies, k, max_candy):
        if max_candy ==0: return True
        total = 0
        for i in candies:
            total += i//max_candy
        return total >= k
    def maximumCandies(self, candies: List[int], k: int) -> int:
        max_el = max(candies)
        left = 0
        right = max_el
        max_candy = 0
        while left <= right:
            mid = left + (right - left)//2
            if self.helper(candies, k , mid):
                max_candy = max(max_candy, mid)
                left = mid + 1
            else:
                right = mid - 1
        return max_candy