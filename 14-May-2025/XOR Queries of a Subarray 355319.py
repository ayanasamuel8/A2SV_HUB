# Problem: XOR Queries of a Subarray - https://leetcode.com/problems/xor-queries-of-a-subarray/

class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        prefix = [0, arr[0]]
        for i in range(1, len(arr)):
            prefix.append(arr[i] ^ prefix[-1])
        ans = []
        for left, right in queries:
            ans.append(prefix[right + 1] ^ prefix[left])
        return ans