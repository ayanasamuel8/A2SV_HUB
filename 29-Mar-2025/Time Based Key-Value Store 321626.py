# Problem: Time Based Key-Value Store - https://leetcode.com/problems/time-based-key-value-store/

class TimeMap:

    def __init__(self):
        self.hashmap = defaultdict(list)
        self.indexmap = defaultdict(str)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hashmap[key].append(timestamp)
        self.indexmap[key +'#' + str(timestamp)] = value

    def get(self, key: str, timestamp: int) -> str:
        if not self.hashmap[key]:
            return ''
        left = bisect_right(self.hashmap[key], timestamp)
        left -= 1
        if left < 0:
            return ''
        else:
            return self.indexmap[key +'#' + str(self.hashmap[key][left])]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)