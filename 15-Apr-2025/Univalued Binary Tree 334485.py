# Problem: Univalued Binary Tree - https://leetcode.com/problems/univalued-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        val = root.val
        queue = deque([root])
        while queue:
            front = queue.popleft()
            if front.left:
                if front.left.val != val:
                    return False
                queue.append(front.left)
            if front.right:
                if front.right.val != val:
                    return False
                queue.append(front.right)
        return True