# Problem: Minimum Operations to Exceed Threshold Value II - https://leetcode.com/problems/minimum-operations-to-exceed-threshold-value-ii/

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        ans=0
        while len(nums)>1:
            min1=heapq.heappop(nums)
            min2=heapq.heappop(nums)
            if(min1>=k and min2>=k): break
            ans+=1
            tot = min(min1,min2) * 2 + max(min1,min2)
            heapq.heappush(nums,tot)
        return ans