# Problem: Interval List Intersections - https://leetcode.com/problems/interval-list-intersections/

class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        left = right = 0
        n, m = len(firstList), len(secondList)
        intersections = []
        
        while left < n and right < m:
            if firstList[left][1] < secondList[right][0]:
                left += 1
            elif firstList[left][0] > secondList[right][1]:
                right += 1
            else:
                start = max(firstList[left][0], secondList[right][0])
                end = min(firstList[left][1], secondList[right][1])
                intersections.append([start, end])
                if secondList[right][1] < firstList[left][1]: right += 1
                else: left += 1
        return intersections