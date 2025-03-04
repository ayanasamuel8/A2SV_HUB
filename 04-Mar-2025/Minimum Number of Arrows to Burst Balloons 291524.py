# Problem: Minimum Number of Arrows to Burst Balloons - https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        n = len(points)
        back = points[0][1]
        count = 1
        for i in range(1,n):
            if back < points[i][0]:
                count += 1
                back = points[i][1]
            back = min(back, points[i][1])
        return count