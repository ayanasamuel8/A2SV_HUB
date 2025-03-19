# Problem: Count Nodes Equal to Average of Subtree - https://leetcode.com/problems/count-nodes-equal-to-average-of-subtree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def count(self,root):
        if not root:
            return 0, 0
        left, num_left = self.count(root.left)
        right, num_right = self.count(root.right)
        if (left + right + root.val) // (num_left + num_right + 1)  == root.val:
            self.cnt += 1
        return (left + right + root.val) , (num_left + num_right + 1)

    def averageOfSubtree(self, root: TreeNode) -> int:
        self.cnt = 0
        self.count(root)
        return self.cnt