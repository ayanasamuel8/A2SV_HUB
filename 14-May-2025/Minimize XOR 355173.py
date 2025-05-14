# Problem: Minimize XOR - https://leetcode.com/problems/minimize-xor/description/

class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        left = bin(num1).count('1')
        right = bin(num2).count('1')
        if left == right:
            return num1
        diff = abs(left - right)
        if left > right:
            i = 0
            while diff:
                if num1 & (1 << i):
                    num1 &= ~(1 << i)
                    diff -= 1
                i += 1
            return num1
        i = 0
        while diff:
            if not num1 & (1 << i):
                num1 |= (1 << i)
                diff -= 1
            i += 1
        return num1