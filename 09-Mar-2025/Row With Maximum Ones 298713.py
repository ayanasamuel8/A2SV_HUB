# Problem: Row With Maximum Ones - https://leetcode.com/problems/row-with-maximum-ones/

class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        ans = [-1,-1]
        index = 0
        for row in mat:
            cnt = row.count(1)
            if cnt > ans[1]:
                ans = [index, cnt]
            index += 1
        return ans