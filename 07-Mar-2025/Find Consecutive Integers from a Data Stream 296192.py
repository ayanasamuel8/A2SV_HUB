# Problem: Find Consecutive Integers from a Data Stream - https://leetcode.com/problems/find-consecutive-integers-from-a-data-stream/

class DataStream:

    def __init__(self, value: int, k: int):
        self.value = value
        self.k = k
        self.data_stream = deque()
        self.difference = 0

    def consec(self, num: int) -> bool:
        self.data_stream.append(num)
        self.difference += num != self.value
        if len(self.data_stream) >= self.k:
            ans = self.difference
            self.difference -= self.data_stream.popleft() != self.value
            return ans == 0
        return False


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)