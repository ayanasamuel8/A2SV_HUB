# Problem: Minimum Time to Repair Cars - https://leetcode.com/problems/minimum-time-to-repair-cars/

class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        n = len(ranks)
        min_el = min(ranks)
        left = 1
        right = min_el * cars * cars
        ans = 0

        def possible(time):
            num_cars = 0
            time_taken = 0
            i = 0
            while i < n:
                num_cars += int(math.sqrt(time//ranks[i]))
                i += 1
            return num_cars >= cars

        while left <= right:
            mid = left + (right - left) //2
            if possible(mid):
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        return ans