# Problem: Maximum Difference Between Node and Ancestor - https://leetcode.com/problems/maximum-difference-between-node-and-ancestor/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDiff(self,root, arr):
        if not root:
            return arr
        arr = [max(arr[0], root.val), min(arr[1], root.val)]
        from_left = [float('-inf'), float('inf')]
        from_right = [float('-inf'), float('inf')]

        from_left = self.maxDiff(root.left, arr.copy())
        from_right = self.maxDiff(root.right, arr.copy())

        if abs(from_left[0] - from_left[1]) > abs(from_right[0] - from_right[1]):
            return from_left
        return from_right
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        result = self.maxDiff(root,[float('-inf'), float('inf')])
        return result[0] - result[1]