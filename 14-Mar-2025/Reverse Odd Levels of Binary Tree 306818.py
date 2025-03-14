# Problem: Reverse Odd Levels of Binary Tree - https://leetcode.com/problems/reverse-odd-levels-of-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverse(self, left, right,inverse):
        if not left: return 
        if inverse:
            leftval = left.val
            left.val = right.val
            right.val = leftval
        self.reverse(left.left, right.right, not inverse)
        self.reverse(left.right, right.left, not inverse)
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.reverse(root.left, root.right, True)
        return root