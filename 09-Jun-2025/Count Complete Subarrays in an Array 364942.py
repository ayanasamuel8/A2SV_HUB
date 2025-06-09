# Problem: Count Complete Subarrays in an Array - https://leetcode.com/problems/count-complete-subarrays-in-an-array/

class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        complete = len(set(nums))
        left = 0
        window = defaultdict(int)
        count = 0
        for right in range(n):
            window[nums[right]] += 1
            while len(window) == complete:
                count += (n - right)
                window[nums[left]] -= 1
                if window[nums[left]] == 0:
                    del window[nums[left]]
                left += 1
        return count