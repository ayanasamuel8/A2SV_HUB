# Problem: Find Unique Binary String - https://leetcode.com/problems/find-unique-binary-string/description/

class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        set_nums = set(nums)
        def backTrack(path):
            if len(path) == len(nums[0]):
                string = ''.join(path)
                if string not in set_nums:
                    return string
                else:
                    return ''
            path.append('0')
            ans = backTrack(path)
            if ans:   return ans
            path.pop()
            path.append('1')
            ans = backTrack(path)
            path.pop()
            return ans
        ans = backTrack([])
        return ans