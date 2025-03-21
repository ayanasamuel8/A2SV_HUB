# Problem: Balance a Binary Search Tree - https://leetcode.com/problems/balance-a-binary-search-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorder(self, root):
        if not root: return []
        result = []
        result.extend(self.inorder(root.left))
        result.append(root.val)
        result.extend(self.inorder(root.right))
        return result
    def constructBST(self, arr):
        if not arr:
            return None
        mid = len(arr) // 2
        root = TreeNode(arr[mid])
        root.left = self.constructBST(arr[:mid])
        root.right = self.constructBST(arr[mid + 1:])
        return root

    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        sortedArr = self.inorder(root)
        return self.constructBST(sortedArr)