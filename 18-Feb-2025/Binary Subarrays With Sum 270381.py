# Problem: Binary Subarrays With Sum - https://leetcode.com/problems/binary-subarrays-with-sum/

class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        n = len(nums)
        # time complexity -> O(2N)
        #space complexity -> O(1)
        def subarrayCount(num):
            if num < 0: return 0
            running_sum = 0
            left = 0
            subarray_count = 0

            for right in range(n):
                running_sum += nums[right]
                while running_sum > num:
                    subarray_count += right - left
                    running_sum -= nums[left]
                    left += 1

            while left < n:
                subarray_count += n - left
                left += 1
            
            return subarray_count
        
        return subarrayCount(goal) - subarrayCount(goal - 1)

        #time complexity -> O(N)
        #space complexity -> O(N)
        '''
        prefix_sum = defaultdict(int)
        prefix_sum[0] = 1
        
        subarray_count = 0 
        running_sum = 0

        for right in range(n):
            running_sum += nums[right]
            subarray_count += prefix_sum[running_sum - goal]
            prefix_sum[running_sum] += 1
        
        return subarray_count
        '''