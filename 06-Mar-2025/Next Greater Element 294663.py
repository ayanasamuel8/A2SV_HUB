# Problem: Next Greater Element - https://leetcode.com/problems/next-greater-element-i/

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        mono_stack = []
        n = len(nums2)
        hashmap = {}
        for i in range(n):
            while mono_stack and mono_stack[-1] < nums2[i]:
                hashmap[mono_stack[-1]] = nums2[i]
                mono_stack.pop()
            mono_stack.append(nums2[i])
        result = []
        for i in nums1:
            if i in hashmap:
                result.append(hashmap[i])
            else:
                result.append(-1)
        return result