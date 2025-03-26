# Problem: Zero Array Transformation II - https://leetcode.com/problems/zero-array-transformation-ii/

class Solution:

    def possible(self, nums, queries, k):
        temp = [0] * (n:=len(nums) + 1)

        #calculating the change in nums using sweep line
        for i in range(k):
            l, r, val = queries[i]
            temp[l] += val
            temp[r + 1] -= val

        #computing prefix sum
        for i in range(1, n):
            temp[i] += temp[i - 1]

        #checking if it can be zero
        for i in range(n - 1):
            if nums[i] - temp[i] > 0:
                return False
        return True


    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        left , right = 0, len(queries)
        ans = -1

        #iterating over all possible answers using binary search
        while left <= right:

            mid = left + (right - left) // 2

            if self.possible(nums, queries, mid):
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        
        return ans