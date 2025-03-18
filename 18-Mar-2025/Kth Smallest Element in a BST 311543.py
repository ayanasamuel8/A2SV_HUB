# Problem: Kth Smallest Element in a BST - https://leetcode.com/problems/kth-smallest-element-in-a-bst/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def counter(self, root, count, k):
        if not root:
            return count, None
        left, f = self.counter(root.left, count,k)
        if left + 1 == k:
            return left + 1, root.val
        if left == k:
            return left,f
        right, f = self.counter(root.right, left  + 1,k)
        return right, f

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        left, ans = self.counter(root, 0, k)
        return ans