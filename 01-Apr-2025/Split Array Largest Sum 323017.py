# Problem: Split Array Largest Sum - https://leetcode.com/problems/split-array-largest-sum/

class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        left, right = 0, sum(nums)

        def possible(guess):
            if max(nums) > guess:
                return False
                
            cnt = 0
            total = 0
            for i in nums:
                total += i
                if total > guess:
                    cnt += 1
                    total = i
            return cnt  + 1 <= k
        
        while left <= right:
            mid = left + (right - left) // 2

            if possible(mid):
                right = mid - 1
            else:
                left =  mid + 1
        
        return left