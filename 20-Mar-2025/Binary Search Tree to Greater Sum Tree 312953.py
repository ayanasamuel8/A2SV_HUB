# Problem: Binary Search Tree to Greater Sum Tree - https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def gstConverter(self, root, val):
        if not root.left and not root.right:
            root.val += val
            return root.val
        if root.right:
            right = self.gstConverter(root.right, val)
            root.val += right
        else:
            root.val += val
        if root.left:
            return self.gstConverter(root.left, root.val)
        return root.val



    def bstToGst(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.gstConverter(root, 0)
        return root