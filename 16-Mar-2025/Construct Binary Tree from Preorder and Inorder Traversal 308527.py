# Problem: Construct Binary Tree from Preorder and Inorder Traversal - https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        hashmap = {val:indx for indx, val in enumerate(inorder)}
        index = 0
        def dfs(left, right):
            nonlocal index
            if left > right:
                return None
            pre = preorder[index]
            root = TreeNode(pre)
            index += 1
            root.left = dfs(left, hashmap[pre] -1)
            root.right = dfs(hashmap[pre] + 1, right)
            
            return root

        return dfs(0,len(preorder) - 1)