# Problem: Maximum Sum BST in Binary Tree - https://leetcode.com/problems/maximum-sum-bst-in-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBST(self, root):
        if not root:
            return 0, True, inf, -inf
        left, isLeft, lmin, lmax = self.isBST(root.left)
        right, isRight, rmin, rmax = self.isBST(root.right)

        if isLeft and isRight and lmax < root.val and rmin > root.val:
            self.max_ans = max(self.max_ans, max(left + right + root.val, left, right))
            return left + right + root.val, True, min(lmin, root.val), max(rmax, root.val)
        self.max_ans = max(self.max_ans, left, right)
        return max(left, right), False, min(lmin, root.val), max(rmax, root.val)


    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        self.max_ans = 0
        ans, _,  _, _ = self.isBST(root)
        return self.max_ans