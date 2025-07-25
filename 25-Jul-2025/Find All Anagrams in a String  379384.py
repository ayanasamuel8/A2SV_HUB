# Problem: Find All Anagrams in a String  - https://leetcode.com/problems/find-all-anagrams-in-a-string/

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        left = 0
        n = len(s)
        ans = []
        p_cntr = Counter(p)
        for right in range(n):
            if s[right] in p_cntr:
                p_cntr -= Counter([s[right]])
            else:
                while left < right and s[right] not in p_cntr:
                    p_cntr[s[left]] += 1
                    left += 1
                if s[right] in p_cntr:
                    p_cntr -= Counter([s[right]])
                elif left == right:
                    left = right + 1
            if not p_cntr:
                ans.append(left)
                p_cntr[s[left]] += 1
                left += 1
        return ans