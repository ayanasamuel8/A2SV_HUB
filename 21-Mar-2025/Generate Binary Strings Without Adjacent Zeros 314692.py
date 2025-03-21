# Problem: Generate Binary Strings Without Adjacent Zeros - https://leetcode.com/problems/generate-binary-strings-without-adjacent-zeros/description/

class Solution:
    def validStrings(self, n: int) -> List[str]:
        result = []
        def backTrack(path):
            if len(path) == n:
                print(path)
                result.append(''.join(path))
                return
            
            if not path or path[-1] != '0':
                path.append('0')
                backTrack(path)
                path.pop()
            path.append('1')
            backTrack(path)
            path.pop()

        backTrack([])

        return result