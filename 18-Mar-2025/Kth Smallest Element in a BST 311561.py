# Problem: Kth Smallest Element in a BST - https://leetcode.com/problems/kth-smallest-element-in-a-bst/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, root):
        if not root:
            return 0
        left = self.solve(root.left)
        if not self.k: 
            return left
        self.k -= 1
        if not self.k: 
            return root.val
        return self.solve(root.right)
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.k = k
        return self.solve(root)