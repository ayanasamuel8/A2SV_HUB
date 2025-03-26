# Problem: Magnetic Force Between Two Balls - https://leetcode.com/problems/magnetic-force-between-two-balls/

class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        n = len(position)
        left, right = 1, max(position) - min(position)

        #checking if it's possible to distribute the ball 
        #by jumping distance : distance
        def possibleToDistribute(distance):
            cnt = 1
            back = position[0]

            for i in range(1,n):
                if position[i] - back >= distance:
                    cnt += 1
                    back = position[i]
            return cnt >= m
        
        while left <= right:
            mid = left + (right - left) // 2
            if possibleToDistribute(mid):
                left = mid + 1
            else:
                right = mid - 1
        return right