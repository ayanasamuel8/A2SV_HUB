# Problem: Camelcase Matching - https://leetcode.com/problems/camelcase-matching/

class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        ans = []
        n = len(queries)
        pl= len(pattern)
        for i in range(n):
            l = len(queries[i])
            if pl > l:
                ans.append(False)
            else:
                left = 0
                for right in range(l):
                    if left < pl and queries[i][right] == pattern[left]:
                        left += 1
                    elif queries[i][right].isupper():
                        ans.append(False)
                        break
                else:
                    ans.append(pl == left)
            
        return ans