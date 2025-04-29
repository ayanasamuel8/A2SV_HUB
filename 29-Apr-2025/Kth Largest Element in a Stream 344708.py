# Problem: Kth Largest Element in a Stream - https://leetcode.com/problems/kth-largest-element-in-a-stream/

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
       self.k = k
       self.nums = []
       for i in nums:
        self.add(i)

    def add(self, val: int) -> int:
        if len(self.nums) < self.k or self.nums[0] < val:
            if len(self.nums) >= self.k: 
                heappop(self.nums)
            heappush(self.nums, val)
        return self.nums[0]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)