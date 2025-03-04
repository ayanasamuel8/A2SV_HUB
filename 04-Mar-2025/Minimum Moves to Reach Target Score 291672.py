# Problem: Minimum Moves to Reach Target Score - https://leetcode.com/problems/minimum-moves-to-reach-target-score/

class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        count = 1 + target % 2
        def moves():
            nonlocal target
            nonlocal count
            nonlocal maxDoubles
            maxDoubles -= 1
            if target <= 1: return 0
            if maxDoubles < 0: return 0
            mod = target % 2
            target //= 2
            return 1 + mod + moves()
        count = moves()
        return count + target - 1