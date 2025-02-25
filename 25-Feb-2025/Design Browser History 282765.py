# Problem: Design Browser History - https://leetcode.com/problems/design-browser-history/description/

class Node:
    def __init__(self,val = 0, next = None , prev = None):
        self.val = val
        self.next = next
        self.prev = prev

class BrowserHistory:

    def __init__(self, homepage: str):
        self.browser_history = Node(homepage)
        self.homepage = self.browser_history

    def visit(self, url: str) -> None:
        new_history = Node(url)
        new_history.prev = self.homepage
        self.homepage.next = new_history
        self.homepage = self.homepage.next

    def back(self, steps: int) -> str:
        while self.homepage.prev and steps:
            self.homepage = self.homepage.prev
            steps -= 1
        return self.homepage.val

    def forward(self, steps: int) -> str:
        while self.homepage.next and steps:
            self.homepage = self.homepage.next
            steps -= 1
        return self.homepage.val


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)