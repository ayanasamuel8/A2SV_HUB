# Problem: Find the Power of K-Size Subarrays II - https://leetcode.com/problems/find-the-power-of-k-size-subarrays-ii/

class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        diff = [1]
        for i in range(1, n):
            if nums[i] == nums[i - 1] + 1:
                diff.append(diff[i - 1] + 1)
            else:
                diff.append(1)
        ans = []
        for i in range(k - 1, n):
            if diff[i] >= k:
                ans.append(nums[i])
            else:
                ans.append(-1)
        return ans