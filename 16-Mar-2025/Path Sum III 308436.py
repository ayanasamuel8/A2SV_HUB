# Problem: Path Sum III - https://leetcode.com/problems/path-sum-iii/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def find(self, path, targetSum):
        total = sum(path)
        ans = total == targetSum
        for i in range(len(path) - 1):
            total -= path[i]
            if total == targetSum:
                ans += 1
        return ans 

    def sumUp(self, root, targetSum, path):
        found = 0
        if not root:
            return found
        path.append(root.val)
        found += self.find(path, targetSum)
        if root.left:
            found += self.sumUp(root.left, targetSum, path)
        if root.right:
            found += self.sumUp(root.right, targetSum, path)
        path.pop()
        return found
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        return self.sumUp(root, targetSum, [])