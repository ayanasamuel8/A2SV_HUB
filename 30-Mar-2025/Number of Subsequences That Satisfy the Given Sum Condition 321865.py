# Problem: Number of Subsequences That Satisfy the Given Sum Condition - https://leetcode.com/problems/number-of-subsequences-that-satisfy-the-given-sum-condition/

class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        MOD = 10**9 + 7
        nums.sort()
        n = len(nums)
        
        pow2 = [1] * (n + 1)
        for i in range(1, n + 1):
            pow2[i] = (pow2[i - 1] * 2) % MOD
        
        left, right = 0, n - 1
        res = 0
        
        while left <= right:
            if nums[left] + nums[right] <= target:
                res = (res + pow2[right - left]) % MOD
                left += 1
            else:
                right -= 1
        
        return res