# Problem: Lowest Common Ancestor of a Binary Search Tree - https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findMin(self, root, min_el, max_el):
        if root.val < min_el and root.val < max_el:
            return self.findMin(root.right,min_el, max_el)
        if root.val > min_el and root.val > max_el:
            return self.findMin(root.left, min_el, max_el)
        return root
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        max_el = max(p.val,q.val)
        min_el = min(q.val,p.val)
        return self.findMin(root, min_el, max_el)