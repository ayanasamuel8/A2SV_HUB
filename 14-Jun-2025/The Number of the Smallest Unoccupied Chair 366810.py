# Problem: The Number of the Smallest Unoccupied Chair - https://leetcode.com/problems/the-number-of-the-smallest-unoccupied-chair/description/

class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        length = len(times)
        free_seats = [i for i in range(length)]
        taken_seats = []
        indexed_times = [(arrival, leaving, idx) for idx, (arrival, leaving) in enumerate(times)]
        indexed_times.sort()

        for i in range(length):
            arrival, leaving, idx = indexed_times[i]
            while taken_seats and taken_seats[0][0] <= arrival:
                left, seat = heappop(taken_seats)
                heappush(free_seats, seat)
            if idx == targetFriend:
                return heappop(free_seats)
            heappush(taken_seats, (leaving, heappop(free_seats)))