# Problem: Find Pivot Index - https://leetcode.com/problems/find-pivot-index/description/

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        presum=0
        aftersum=sum(nums[1:])
        for i in range(len(nums)-1):
            if presum==aftersum:
                return i
            else:
                presum+=nums[i]
                aftersum-=nums[i+1]
        if sum(nums[:-1])==0:
            return len(nums)-1
        return -1