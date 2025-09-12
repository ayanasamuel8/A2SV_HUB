# Problem: Sum of Even Numbers After Queries - https://leetcode.com/problems/sum-of-even-numbers-after-queries/description/

class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        ans = []
        sum_ = [0, 0]
        for i in nums:
            sum_[i % 2] += i
        
        for val, index in queries:
            sum_[nums[index] % 2] -= nums[index]
            nums[index] += val
            sum_[nums[index] % 2] += nums[index]
            ans.append(sum_[0])
        
        return ans