# Problem: House Robber IV - https://leetcode.com/problems/house-robber-iv/

class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        left = min(nums)
        right = max(nums)

        def check(n):
            count = 0
            i = 0
            while i < len(nums):
                if nums[i] <= n:
                    count += 1
                    i += 1
                i += 1
            return count >= k

        while left <= right:
            mid = left + (right - left) // 2
            if check(mid):
                right = mid - 1
            else:
                left = mid + 1
        return left