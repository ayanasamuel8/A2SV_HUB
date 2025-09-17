# Problem: Super Pow - https://leetcode.com/problems/super-pow/description/

class Solution:
    def mod(self, a):
        return a % 1337

    def calculate(self, a, b, c):
        curr = pow(self.mod(a), b, 1337)
        while c:
            curr = pow(curr, 10, 1337)
            c -= 1
        return curr

    def superPow(self, a: int, b: List[int]) -> int:
        total = 1
        n = len(b)
        b.reverse()
        for i in range(n):
            if b[i] != 0:
                total = self.mod(self.mod(total) * self.mod(self.calculate(a, b[i], i)))
        
        return total