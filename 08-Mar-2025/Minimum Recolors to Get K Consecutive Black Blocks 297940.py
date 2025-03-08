# Problem: Minimum Recolors to Get K Consecutive Black Blocks - https://leetcode.com/problems/minimum-recolors-to-get-k-consecutive-black-blocks/

class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        n = len(blocks)
        w_count = 0
        b_count = 0
        for i in range(k):
            w_count += blocks[i] == 'W'
        min_len = w_count
        for i in range(k,n):
            w_count -= blocks[i - k] == 'W'
            w_count += blocks[i] == 'W'
            min_len = min(min_len, w_count)
        return min_len