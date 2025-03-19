# Problem: Merge Two Binary Trees - https://leetcode.com/problems/merge-two-binary-trees/

class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root2:
            return root1
        if not root1:
            return root2
            
        root = TreeNode(root1.val + root2.val)
        root.left = self.mergeTrees(root1.left, root2.left)
        root.right = self.mergeTrees(root1.right, root2.right)

        return root