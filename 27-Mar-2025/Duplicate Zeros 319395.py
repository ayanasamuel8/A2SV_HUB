# Problem: Duplicate Zeros - https://leetcode.com/problems/duplicate-zeros/description/?envType=problem-list-v2&envId=two-pointers

class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        num_zero = arr.count(0)
        if not num_zero:
            return
        
        n = len(arr)
        arr.extend([0] * num_zero)
        right = len(arr) - 1
        
        for left in range(n - 1, -1, -1):
            if arr[left]:
                arr[left], arr[right] = arr[right], arr[left]
            else:
                right -= 1
            right -= 1
        arr[:] = arr[:n]