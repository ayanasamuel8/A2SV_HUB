# Problem: Height Checker
(Easy) - https://leetcode.com/problems/height-checker/

class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        cnt = 0
        n = len(heights)
        srted = sorted(heights)
        for i in range(n):
            if srted[i] != heights[i]:
                cnt += 1
        return cnt