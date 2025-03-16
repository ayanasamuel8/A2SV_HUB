# Problem: Same Tree - https://leetcode.com/problems/same-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def oneOfThem(self, root1, root2):
        if root1 and not root2 or root2 and not root1: return True
        return False
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q: return True
        elif self.oneOfThem(q,p): return False
        print(q.val, p.val)
        if q.val != p.val:
            return False
        if p.left and q.left:
            if not self.isSameTree(q.left,p.left):
                return False
        elif self.oneOfThem(q.left, p.left):
            return False
        if q.right and p.right:
            if not self.isSameTree(q.right, p.right):
                return False
        elif self.oneOfThem(q.right,p.right):
            return False
        return True