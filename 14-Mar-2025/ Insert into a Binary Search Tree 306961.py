# Problem:  Insert into a Binary Search Tree - https://leetcode.com/problems/insert-into-a-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insert(self, root, val):
        if root.val >= val:
            if not root.left:
                root.left = TreeNode(val)
                return
            self.insert(root.left, val)
        else:
            if not root.right:
                root.right = TreeNode(val)
                return
            self.insert(root.right, val)
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root: return TreeNode(val)
        self.insert(root, val)
        return root