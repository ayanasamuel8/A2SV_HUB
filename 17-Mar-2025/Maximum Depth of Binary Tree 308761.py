# Problem: Maximum Depth of Binary Tree - https://leetcode.com/problems/maximum-depth-of-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def depth(self, root, index):
        if not root:
            return index
        return max(self.depth(root.left, index + 1), self.depth(root.right, index + 1))
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.depth(root, 0)