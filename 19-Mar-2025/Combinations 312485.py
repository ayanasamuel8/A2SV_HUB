# Problem: Combinations - https://leetcode.com/problems/combinations/

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        def backTrack(path, curr):
            if len(path) == k:
                result.append(path.copy())
                return
            for i in range(curr + 1,n+1):
                path.append(i)
                backTrack(path, i)
                path.pop()
        backTrack([],0)
        return result