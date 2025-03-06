# Problem: Number of Recent Calls - https://leetcode.com/problems/number-of-recent-calls/

class RecentCounter:

    def __init__(self):
        self.recent = deque()

    def ping(self, t: int) -> int:
        while self.recent and self.recent[0] < t - 3000:
            self.recent.popleft()
        self.recent.append(t)
        return len(self.recent)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)