# Problem: Subarrays with K Different Integers - https://leetcode.com/problems/subarrays-with-k-different-integers/

class Solution:
    def subarraysWithAtleastKDistinct(self, nums, k):
        left = 0
        n = len(nums)
        distinct = Counter()
        total = 0
        for right in range(n):
            distinct[nums[right]] += 1
            while len(distinct) == k:
                distinct -= Counter([nums[left]])
                left += 1
            total += left
        return total

    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        with_k = self.subarraysWithAtleastKDistinct(nums, k)
        with_k_p_1 = self.subarraysWithAtleastKDistinct(nums, k + 1)
        return with_k - with_k_p_1