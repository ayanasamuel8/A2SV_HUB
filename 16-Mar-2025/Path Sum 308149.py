# Problem: Path Sum - https://leetcode.com/problems/path-sum/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumUp(self, root, targetSum, currSum):
        currSum += root.val
        if not root.left and not root.right:
            return currSum == targetSum

        from_left = False
        if root.left:
            from_left = self.sumUp(root.left, targetSum,currSum)
        if from_left: return True

        from_right = False
        if root.right:
            from_right = self.sumUp(root.right, targetSum, currSum)

        return from_right

    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root: return False
        return self.sumUp(root, targetSum, 0)