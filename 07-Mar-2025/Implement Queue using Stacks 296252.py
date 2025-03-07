# Problem: Implement Queue using Stacks - https://leetcode.com/problems/implement-queue-using-stacks/

class MyQueue:

    def __init__(self):
        self.front_stack = []
        self.back_stack = []

    def push(self, x: int) -> None:
        self.back_stack.append(x)
        self.front_stack = self.back_stack[::-1]

    def pop(self) -> int:
        val = self.front_stack.pop()
        self.back_stack = self.front_stack[::-1]
        return val

    def peek(self) -> int:
        return self.front_stack[-1]

    def empty(self) -> bool:
        return not self.front_stack


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()