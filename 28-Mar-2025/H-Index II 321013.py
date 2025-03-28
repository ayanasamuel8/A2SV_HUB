# Problem: H-Index II - https://leetcode.com/problems/h-index-ii/description/

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        left, right = 0, ((n:= len(citations)) - 1)
    
        while left < right:
            mid = left + (right - left) // 2

            if citations[mid] >= (n - mid):
                right = mid
            else:
                left = mid + 1
                
        return n-right if citations[right] >= n - right else 0
