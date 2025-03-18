# Problem: Validate Binary Search Tree - https://leetcode.com/problems/validate-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def validate(self, root):
        min_el = float('inf')
        max_el = float('-inf')
        if root.left:
            left_min,left_max, state = self.validate(root.left)
            min_el = min(min_el, left_min, left_max)

            if not state or left_min >= root.val or left_max >= root.val:
                return root.val,left_min, False
        if root.right:
            right_min,right_max,state = self.validate(root.right)
            max_el = max(max_el, right_min, right_max)

            if not state or right_min <= root.val or right_max <= root.val:
                return root.val,right_min, False

        return min(min_el, root.val),max(max_el, root.val), True

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        *ele, state = self.validate(root)
        return state