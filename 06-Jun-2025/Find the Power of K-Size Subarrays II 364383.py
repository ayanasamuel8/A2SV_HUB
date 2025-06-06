# Problem: Find the Power of K-Size Subarrays II - https://leetcode.com/problems/find-the-power-of-k-size-subarrays-ii/

class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        diff = [1] * (n:=len(nums))
        for i in range(1, n):
            if nums[i] == nums[i - 1] + 1:
                diff[i] = diff[i - 1] + 1
            
        ans = [-1] * (n - k + 1)
        
        for i in range(k - 1, n):
            if diff[i] >= k:
                ans[i - k + 1] = nums[i]

        return ans