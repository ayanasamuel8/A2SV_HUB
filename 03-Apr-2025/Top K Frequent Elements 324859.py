# Problem: Top K Frequent Elements - https://leetcode.com/problems/top-k-frequent-elements/

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n=len(nums)
        nums_counter=Counter(nums)
        bucket=[[]*n for _ in range(n)]
        for key,value in nums_counter.items():
            bucket[value-1].append(key)
        ans=[]
        for i in range(n-1,-1,-1):
            bucket_size =len(ans)+len(bucket[i])
            if bucket_size<=k:
                ans.extend(bucket[i])
            else:
                ans.extend(bucket[i][:bucket_size-k-1])
            if len(ans)==k: break
        return ans