# Problem: Count Vowel Strings in Ranges - https://leetcode.com/problems/count-vowel-strings-in-ranges/

class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels = 'aeiou'
        prefix = [0]
        for word in words:
            if word[0] in vowels and word[-1] in vowels:
                prefix.append(1)
            else:
                prefix.append(0)
        for i in range(1, len(prefix)):
            prefix[i] += prefix[i -1]
        
        ans = []
        for l, r in queries:
            ans.append(prefix[r + 1] - prefix[l])
        return ans