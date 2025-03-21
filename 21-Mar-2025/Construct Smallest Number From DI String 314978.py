# Problem: Construct Smallest Number From DI String - https://leetcode.com/problems/construct-smallest-number-from-di-string/description/

class Solution:
    def smallestNumber(self, pattern: str) -> str:
        used = set()
        result = []
        ans = ''
        def backTrack(path):
            nonlocal ans
            if len(path) == len(pattern) + 1:
                ans = ''.join(map(str, path))
                return True
            
            start = 1
            end = 10
            if pattern[len(path) - 1] == 'I':
                start = path[-1] + 1
            else:
                end = path[-1]
            
            for i in range(start,end):
                if i not in used:
                    path.append(i)
                    used.add(i)
                    if backTrack(path):
                        return True
                    path.pop()
                    used.remove(i)

            return False
        for i in range(1,10):
            used.add(i)
            if backTrack([i]):
                break
            used.remove(i)

        return ans