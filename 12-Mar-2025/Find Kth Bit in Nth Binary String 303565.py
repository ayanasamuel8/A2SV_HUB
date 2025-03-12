# Problem: Find Kth Bit in Nth Binary String - https://leetcode.com/problems/find-kth-bit-in-nth-binary-string/

class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def invert(string):
            arr = []
            for i in string:
                arr.append(str(1 ^ int(i)))
            return arr[::-1]
        def stringFormation(string):
            if len(string) >= k:
                return string[k - 1]
            inverted = invert(string)
            string.append('1')
            string.extend(inverted)
            return stringFormation(string)
        return stringFormation(['0'])