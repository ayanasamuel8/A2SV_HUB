# Problem: Binary Tree Paths - https://leetcode.com/problems/binary-tree-paths/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def drawPath(self, root, result, path):
        path.append(root.val)

        if not root.left and not root.right:
            result.append('->'.join(map(str,path)))
        
        if root.left:
            self.drawPath(root.left, result, path.copy())
        if root.right:
            self.drawPath(root.right, result, path.copy())
    

    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        result = []
        self.drawPath(root, result, [])
        return result