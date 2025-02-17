# Problem: Range Sum Query - Immutable - https://leetcode.com/problems/range-sum-query-immutable/

class NumArray:

    def __init__(self, nums: List[int]):
        self.array = [0]*(len(nums)+1)
        for i in range(len(nums)):
            self.array[i+1] = self.array[i] + nums[i]

    def sumRange(self, left: int, right: int) -> int:
        return self.array[right+1]-self.array[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)