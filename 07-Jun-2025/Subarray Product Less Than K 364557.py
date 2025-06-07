# Problem: Subarray Product Less Than K - https://leetcode.com/problems/subarray-product-less-than-k/

class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        prefix_product = [1]
        
        for i in nums:
            prefix_product.append(prefix_product[-1] * i)
        
        left = 0
        num_subarray = 0
        
        for right in range(1, len(nums) + 1):
            while left < right and prefix_product[right] // prefix_product[left] >= k:
                left += 1
            if left == right:
                num_subarray += int(nums[right - 1] < k)
            else:
                num_subarray += right - left
       
        return num_subarray