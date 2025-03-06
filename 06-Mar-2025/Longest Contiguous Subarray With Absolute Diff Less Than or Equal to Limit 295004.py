# Problem: Longest Contiguous Subarray With Absolute Diff Less Than or Equal to Limit - https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        queue = deque()
        max_queue =deque()
        n = len(nums)
        left = 0
        max_len = 0
        for i in range(n):
            while queue and nums[queue[-1]] > nums[i]:
                queue.pop()
            while max_queue and nums[max_queue[-1]] < nums[i]:
                max_queue.pop()
            queue.append(i)
            max_queue.append(i)
            while queue and max_queue and nums[max_queue[0]] - nums[queue[0]] > limit:
                if queue[0] < max_queue[0]: 
                    left = queue.popleft() + 1
                else: 
                    left = max_queue.popleft() + 1
            max_len = max(max_len, i - left + 1)
        return max_len
