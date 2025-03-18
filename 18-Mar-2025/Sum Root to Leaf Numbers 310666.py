# Problem: Sum Root to Leaf Numbers - https://leetcode.com/problems/sum-root-to-leaf-numbers/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumUp(self, root, currSum):
        if not root.left and not root.right:
            num = 0
            for i in currSum:
                num = num * 10 + i
            num = num * 10 + root.val
            return num
        currSum.append(root.val)
        left = 0
        if root.left:
            left = self.sumUp(root.left, currSum)
        right = 0
        if root.right:
            right = self.sumUp(root.right, currSum)
        currSum.pop()
        return left + right
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        return self.sumUp(root, [])