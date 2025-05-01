# Problem: Furthest Building You Can Reach - https://leetcode.com/problems/furthest-building-you-can-reach/

class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        min_heap = []
        brick_count = 0
        i = 0
        while i < len(heights) - 1:
            if heights[i] > heights[i + 1]:
                i += 1
                continue
            heappush(min_heap, (heights[i + 1] - heights[i]))
            if len(min_heap) > ladders:
                brick_count += heappop(min_heap)
                if brick_count > bricks:
                    return i
            i += 1
        return i