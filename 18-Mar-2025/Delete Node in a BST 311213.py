# Problem: Delete Node in a BST - https://leetcode.com/problems/delete-node-in-a-bst/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findNode(self, root, targetVal):
        if not root:
            return None
        if root.val == targetVal:
            result = self.findSuccessor(root.right, root, True)
            if result:
                result.left = root.left
                result.right = root.right
                return result
    
            return root.left
        result = root
        if root.val < targetVal:
            result.left = root.left
            result.right = self.findNode(root.right, targetVal)
            return result
        if root.val > targetVal:
            result.right = root.right
            result.left = self.findNode(root.left, targetVal)
            return result

    def findSuccessor(self, root, parent, right):
        if not root: return None
        if not root.left:
            val = root
            if not right:
                parent.left = root.right
            else:
                parent.right = root.right
            return val
        return self.findSuccessor(root.left, root, False)

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        return self.findNode(root, key)