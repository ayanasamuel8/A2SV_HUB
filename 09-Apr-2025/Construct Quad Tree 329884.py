# Problem: Construct Quad Tree - https://leetcode.com/problems/construct-quad-tree/description/

"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def allValuesTheSame(self,grid):
        start = grid[0][0]
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] != start:
                    return False
        return True


    def construct(self, grid: List[List[int]]) -> 'Node':
        if self.allValuesTheSame(grid):
            return Node(grid[0][0], True, None, None,None,None)
        else:
            n = len(grid)
            half = n // 2
            root = Node(0, False, None, None,None,None)
            root.topLeft = self.construct([row[:half] for row in grid[:half]])
            root.topRight = self.construct([row[half:] for row in grid[:half]])
            root.bottomLeft = self.construct([row[:half] for row in grid[half:]])
            root.bottomRight = self.construct([row[half:] for row in grid[half:]])
            return root