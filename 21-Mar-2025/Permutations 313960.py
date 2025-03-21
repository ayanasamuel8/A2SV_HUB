# Problem: Permutations - https://leetcode.com/problems/permutations/

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        parent = set()
        result =[]
        def backTrack(path):
            if len(path) == len(nums):
                result.append(path.copy())
                return
            for i in nums:
                if i not in parent:
                    parent.add(i)
                    path.append(i)
                    backTrack(path)
                    path.pop()
                    parent.remove(i)
        backTrack([])
        return result