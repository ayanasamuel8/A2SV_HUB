# Problem: Find Largest Value in Each Tree Row - https://leetcode.com/problems/find-largest-value-in-each-tree-row/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largest(self, result, root,index):
        if not root: return
        result[index] = max(result[index], root.val)
        if root.left:
            if len(result) == index + 1:
                result.append(float('-inf'))
            self.largest(result, root.left, index + 1)
        if root.right:
            if len(result) == index + 1:
                result.append(float('-inf'))
            self.largest(result, root.right, index + 1)
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        result = [float('-inf')]
        self.largest(result, root, 0)
        return result if root else []

