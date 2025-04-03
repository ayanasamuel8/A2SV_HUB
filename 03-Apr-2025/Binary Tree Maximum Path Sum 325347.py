# Problem: Binary Tree Maximum Path Sum - https://leetcode.com/problems/binary-tree-maximum-path-sum/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root):
        if not root:
            return -inf
        left = self.pathSum(root.left)
        right = self.pathSum(root.right)
        self.max_path = max(self.max_path, root.val + left + right, left, right, root.val, root.val + right, root.val + left)
        return max(root.val + (max(left, right)), root.val)

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_path = -inf
        self.pathSum(root)
        return self.max_path