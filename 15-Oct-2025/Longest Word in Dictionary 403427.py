# Problem: Longest Word in Dictionary - https://leetcode.com/problems/longest-word-in-dictionary/

class Trie:
    def __init__(self):
        self.words = [None] * 26
        self.is_word = False
    
    def add(self, word):
        root = self
        is_full = True
        n = len(word)
        for i, w in enumerate(word):
            ch = ord(w) - 97
            if not root.words[ch]:
                root.words[ch] = Trie()
            root = root.words[ch]
            if i != n - 1:
                is_full &= root.is_word
        root.is_word = True
        return is_full

class Solution:
    def longestWord(self, words: List[str]) -> str:
        words.sort()
        ans = ""
        t = Trie()
        for word in words:
            is_full = t.add(word)
            if is_full:
                ans = max(ans, word, key=len)
        return ans