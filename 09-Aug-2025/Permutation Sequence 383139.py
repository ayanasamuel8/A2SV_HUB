# Problem: Permutation Sequence - https://leetcode.com/problems/permutation-sequence/description/

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        result = []
        seen = [False] * (n + 1)
        def backTrack(path):
            if len(path) == n:
                result.append(path[:])
            if len(result) > k:
                return
            for i in range(1, n + 1):
                if not seen[i] :
                    path.append(i)
                    seen[i] = True
                    backTrack(path)
                    seen[i] = False
                    path.pop()
        backTrack([])
        ans = result[k - 1]
        return ''.join(map(str,ans))