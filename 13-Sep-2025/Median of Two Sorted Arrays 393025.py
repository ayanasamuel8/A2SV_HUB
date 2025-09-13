# Problem: Median of Two Sorted Arrays - https://leetcode.com/problems/median-of-two-sorted-arrays/

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n, m = len(nums1), len(nums2)
        is_odd = bool((n + m) % 2)
        half = (n + m + 1) // 2
        high = half
        low = 0
        while low <= high:
            from_first = low + (high - low) // 2
            from_second = half - from_first
            if n < from_first:
                high = from_first - 1
            elif m < from_second:
                low = from_first + 1
            elif from_first > 0 and m > from_second and  nums1[from_first - 1] > nums2[from_second]:
                high = from_first - 1
            elif from_second > 0 and n > from_first and nums2[from_second - 1] > nums1[from_first]:
                low = from_first + 1
            else:
                break
        
        if is_odd:
            return max(
                nums1[from_first - 1] if from_first > 0 else -inf,
                nums2[from_second - 1] if from_second > 0 else -inf
            )
        return (
            max(
                nums1[from_first - 1] if from_first > 0 else -inf,
                nums2[from_second - 1] if from_second > 0 else -inf
            ) +
            min(
                nums1[from_first] if from_first < n else inf,
                nums2[from_second] if from_second < m else inf
            )
        ) / 2