# Problem: Find Consecutive Integers from a Data Stream - https://leetcode.com/problems/find-consecutive-integers-from-a-data-stream/

class DataStream:

    def __init__(self, value: int, k: int):
        self.value = value
        self.k = k
        self.lastInteger =0

    def consec(self, num: int) -> bool:
        if num == self.value:
            self.lastInteger += 1
        else:
            self.lastInteger = 0
        return self.lastInteger >= self.k


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)