# Problem: Count Number of Maximum Bitwise-OR Subsets - https://leetcode.com/problems/count-number-of-maximum-bitwise-or-subsets/description/

class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        max_or = reduce(lambda a, b: a | b, nums)
        n = len(nums)
        self.count = 0
        def count_subset(index, curr_or):
            if index == n:
                return
            count_subset(index + 1, curr_or)
            curr_or |= nums[index]
            if curr_or == max_or:
                self.count += 1
            count_subset(index + 1, curr_or)
        count_subset(0, 0)
        return self.count