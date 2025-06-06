# Problem: Zero Array Transformation III - https://leetcode.com/problems/zero-array-transformation-iii/description/

class Solution:
    def maxRemoval(self, nums: List[int], queries: List[List[int]]) -> int:
        queries.sort()
        max_heap = []
        n = len(nums)
        diff_arr = [0] * (n + 1)
        m = len(queries)
        j = 0
        running_sum = 0
        for i in range(n):
            while j < m and queries[j][0] == i:
                heapq.heappush(max_heap, (-queries[j][1], queries[j][0]))
                j += 1
            running_sum += diff_arr[i]
            while max_heap and running_sum < nums[i] and -max_heap[0][0] >= i:
                u, v = heapq.heappop(max_heap)
                diff_arr[-u + 1] -= 1
                diff_arr[v] += 1
                running_sum += 1
            if running_sum < nums[i]:
                return -1
        return len(max_heap)
            