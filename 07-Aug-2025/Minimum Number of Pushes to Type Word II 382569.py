# Problem: Minimum Number of Pushes to Type Word II - https://leetcode.com/problems/minimum-number-of-pushes-to-type-word-ii/

class Solution:
    def minimumPushes(self, word: str) -> int:
        cntr = Counter(word)
        sorted_cntr = sorted([i for i in cntr.values()], reverse=True)
        start = 8
        total = 0
        for i in sorted_cntr:
            total += ((start // 8) * i)
            start += 1
        return total