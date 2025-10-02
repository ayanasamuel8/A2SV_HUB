# Problem: Count Vowel Strings in Ranges - https://leetcode.com/problems/count-vowel-strings-in-ranges/

class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels = 'aeiou'
        prefix = [0]
        for word in words:
            prefix.append(prefix[-1] + (word[0] in vowels and word[-1] in vowels))
        
        ans = []
        for l, r in queries:
            ans.append(prefix[r + 1] - prefix[l])
        return ans