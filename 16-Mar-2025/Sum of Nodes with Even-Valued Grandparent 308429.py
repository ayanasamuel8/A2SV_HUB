# Problem: Sum of Nodes with Even-Valued Grandparent - https://leetcode.com/problems/sum-of-nodes-with-even-valued-grandparent/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root, parent, currSum):
        if not root: 
            return currSum
        if len(parent) == 2:
            if not parent[0] % 2: 
                currSum += root.val
            parent.popleft()
        parent.append(root.val)
        left = right = 0
        if root.left:
            left = self.pathSum(root.left, parent.copy(), 0)
        if root.right:
            right = self.pathSum(root.right,parent.copy(), 0)
        return right + left + currSum
    def sumEvenGrandparent(self, root: Optional[TreeNode]) -> int:
        return self.pathSum(root, deque(), 0)