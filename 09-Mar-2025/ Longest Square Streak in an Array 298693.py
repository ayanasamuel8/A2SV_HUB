# Problem:  Longest Square Streak in an Array - https://leetcode.com/problems/longest-square-streak-in-an-array/description/?envType=problem-list-v2&envId=sorting

class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        set_nums = set(nums)
        n = len(nums)
        seen = set()
        ans = -1

        for i in set_nums:

            count = 0

            if i not in seen:

                count += 1
                seen.add(i)
                curr = i

                while curr ** 2 in set_nums:
                    count += 1
                    curr **= 2
                    seen.add(curr)

            if count > 1:
                ans = max(ans, count)
                
        return ans