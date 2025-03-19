# Problem: Combinations - https://leetcode.com/problems/combinations/

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        seen = [0] * n
        def backTrack(path, curr):
            if len(path) == k:
                result.append(path.copy())
                return
            for i in range(curr + 1,n+1):
                if not seen[i - 1]:
                    path.append(i)
                    seen[i - 1] = True
                    backTrack(path, i)
                    path.pop()
                    seen[i - 1] = False
        backTrack([],0)
        return result