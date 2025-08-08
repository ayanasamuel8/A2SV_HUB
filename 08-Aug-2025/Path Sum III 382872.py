# Problem: Path Sum III - https://leetcode.com/problems/path-sum-iii/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumUp(self, root, targetSum, path, currSum):
        found = 0
        if not root:
            return found
        currSum += root.val
        found += path[currSum - targetSum]
        path[currSum] += 1
        if root.left:
            found += self.sumUp(root.left, targetSum, path,currSum)
        if root.right:
            found += self.sumUp(root.right, targetSum, path,currSum)
        path[currSum] -= 1
        return found
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        dic = defaultdict(int)
        dic[0] = 1
        return self.sumUp(root, targetSum, dic, 0)