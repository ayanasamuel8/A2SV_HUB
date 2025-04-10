# Problem: Number of Pairs Satisfying Inequality - https://leetcode.com/problems/number-of-pairs-satisfying-inequality/

class Solution:
    def mergeSort(self, left, right, arr,diff):
        if left == right:
            return [arr[left]]
        
        mid = (left + right) // 2
        left_half = self.mergeSort(left, mid, arr, diff)
        right_half = self.mergeSort(mid + 1, right, arr, diff)

        self.total += self.countPairs(left_half, right_half, diff)
        return self.merge(left_half, right_half)
    
    def countPairs(self, left_half, right_half, diff):
        left = right = 0
        n, m = len(left_half), len(right_half)
        count = 0

        while left < n and right < m:
            if right_half[right] >= left_half[left] - diff:
                count += m - right
                left += 1
            else:
                right += 1
        return count

    
    def merge(self, left_half, right_half):
        left = right = 0
        n, m = len(left_half), len(right_half)
        merged = []
        while left < n and right < m:
            if left_half[left] <= right_half[right]:
                merged.append(left_half[left])
                left += 1
            else:
                merged.append(right_half[right])
                right += 1
        merged.extend(left_half[left:])
        merged.extend(right_half[right:])
        return merged

    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        n = len(nums1)
        difference_arr = [nums1[i] - nums2[i] for i in range(n)]

        self.total = 0
        self.mergeSort(0, n - 1, difference_arr,diff)

        return self.total          
