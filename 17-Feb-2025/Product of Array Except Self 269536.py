# Problem: Product of Array Except Self - https://leetcode.com/problems/product-of-array-except-self/

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix_product = [1]*(n+1)
        suffix_product = [1] *(n + 1)

        for i in range(n):
            prefix_product[i + 1] = prefix_product[i] * nums[i]
            suffix_product[i + 1] = suffix_product[i] * nums[n - i - 1]
        
        product_of_array = []
        for i in range(n):
            product_of_array.append(prefix_product[i] * suffix_product[n - i-1])
        
        return product_of_array