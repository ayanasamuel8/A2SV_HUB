# Problem: Heaters - https://leetcode.com/problems/heaters/

class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        heaters.sort()
        houses.sort()
        left, right = 0, max(max(houses), max(heaters))
        answer = right

        def isPossible(radius):
            i = 0
            for house in houses:
                while i < len(heaters) and heaters[i] < house - radius:
                    i += 1
                if i >= len(heaters) or heaters[i] > house + radius:
                    return False
            return True

        while left <= right:
            mid = left + (right - left) // 2
            if isPossible(mid):
                answer = mid
                right = mid - 1
            else:
                left = mid + 1
        return answer