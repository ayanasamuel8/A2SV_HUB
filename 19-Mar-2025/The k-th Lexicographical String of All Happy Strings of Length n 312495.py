# Problem: The k-th Lexicographical String of All Happy Strings of Length n - https://leetcode.com/problems/the-k-th-lexicographical-string-of-all-happy-strings-of-length-n/description/

class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        string = 'abc'
        result = []
        seen = set()

        def backTrack(path):
            if len(path) == n+1:
                result.append(''.join(path[1:]))
                return
            for i in range(3):
                if path[-1] != string[i]:
                    path.append(string[i])
                    backTrack(path)
                    path.pop()
            return
        backTrack([0])
        return result[k-1] if k-1<len(result) else ''