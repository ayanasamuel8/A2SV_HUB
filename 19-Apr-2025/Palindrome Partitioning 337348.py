# Problem: Palindrome Partitioning - https://leetcode.com/problems/palindrome-partitioning/

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []
        n = len(s)

        def isPalindrome(string):
            left, right = 0, len(string) - 1
            while left < right:
                if string[left] != string[right]:
                    return False
                left += 1
                right -= 1
            return True
        
        def backTrack(path, string):
            if not string:
                result.append(path.copy())
                return
            for i in range(1, len(string) + 1):
                if isPalindrome(string[:i]):
                    path.append(string[:i])
                    backTrack(path, string[i:])
                    path.pop()
        
        backTrack([], s)
        return result
