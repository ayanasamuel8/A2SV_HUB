# Problem: Max Consecutive Ones III - https://leetcode.com/problems/max-consecutive-ones-iii/

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        zero_count=0
        left=0
        n=len(nums)
        ans=0
        for right in range(n):
            zero_count+=not nums[right]
            while zero_count>k:
                zero_count-=not nums[left]
                left+=1
            ans=max(ans,right-left+1)
        return ans