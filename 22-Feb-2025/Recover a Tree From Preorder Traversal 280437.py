# Problem: Recover a Tree From Preorder Traversal - https://leetcode.com/problems/recover-a-tree-from-preorder-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        index = 0
        def dfs(root, dashes):
            nonlocal index
            integer = 0
            while index < len(traversal) and traversal[index].isdigit():
                integer = (integer * 10) + int(traversal[index])
                index += 1
            root.val = integer
            new_dashes = 0
            while index < len(traversal) and traversal[index] == '-':
                new_dashes += 1
                index += 1
            if new_dashes < dashes: 
                index -= new_dashes
                return root
            root.left = dfs(TreeNode(),dashes + 1)
            new_dashes = 0
            while index < len(traversal) and traversal[index] == '-':
                new_dashes += 1
                index += 1
            if new_dashes < dashes: 
                index -= new_dashes
                return root
            root.right = dfs(TreeNode(), dashes + 1)
            return root
        root = dfs(TreeNode(),1)
        return root