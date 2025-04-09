# Problem: Find Champion II - https://leetcode.com/problems/find-champion-ii/

class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        indegree = [0] * n
        for u, v in edges:
            indegree[v] += 1
        
        candidate = -1
        for i in range(n):
            if indegree[i] == 0:
                if candidate == -1:
                    candidate = i
                else:
                    return -1
        return candidate