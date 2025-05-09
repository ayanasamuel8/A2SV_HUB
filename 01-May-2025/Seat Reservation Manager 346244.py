# Problem: Seat Reservation Manager - https://leetcode.com/problems/seat-reservation-manager/description/

class SeatManager:

    def __init__(self, n: int):
        self.min_heap = [i + 1 for i in range(n)]
        heapify(self.min_heap)

    def reserve(self) -> int:
        return heappop(self.min_heap)

    def unreserve(self, seatNumber: int) -> None:
        heappush(self.min_heap, seatNumber)


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)