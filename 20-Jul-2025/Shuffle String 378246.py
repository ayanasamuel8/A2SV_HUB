# Problem: Shuffle String - https://leetcode.com/problems/shuffle-string/description/

class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        res = [0] * len(s)
        for i,v in enumerate(s):
            res[indices[i]] =v
        return ''.join(res)
        