# Problem: Heap Sort - https://practice.geeksforgeeks.org/problems/heap-sort/1

class Solution:
    def heapSort(self, arr):
        def heapify(n, i):
            largest = i
            left = 2 * i + 1
            right = 2 * i + 2
            if left < n and arr[left] > arr[largest]:
                largest = left
            if right < n and arr[right] > arr[largest]:
                largest = right
            if largest != i:
                arr[largest], arr[i] = arr[i], arr[largest]
                heapify(n, largest)
        
        n = len(arr)
        for i in range(n//2 - 1, -1, -1):
            heapify(n, i)
        
        for i in range(n - 1, 0, -1):
            arr[0], arr[i] = arr[i], arr[0]
            heapify(i, 0)