# Problem: Relative Sort Array - https://leetcode.com/problems/relative-sort-array/description/

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        start=0
        for i in range(len(arr2)):
            for j in range(start,len(arr1)):
                if arr1[j]==arr2[i]:
                    arr1[j],arr1[start]=arr1[start],arr1[j]
                    start+=1
        arr1=arr1[:start]+sorted(arr1[start:])
        return arr1