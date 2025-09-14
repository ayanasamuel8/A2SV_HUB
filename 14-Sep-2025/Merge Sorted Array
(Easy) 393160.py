# Problem: Merge Sorted Array
(Easy) - https://leetcode.com/problems/merge-sorted-array/

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        l=0
        while l<len(nums1) and len(nums2)>0:
            if nums1[l]>nums2[0]:
                nums1.insert(l,nums2[0])
                nums1.pop()
                nums2.remove(nums2[0])
            l+=1
        if len(nums2)>0:
            nums1[len(nums1)-len(nums2):]=nums2