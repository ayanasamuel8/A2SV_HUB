# Problem: Maximum Score Words Formed by Letters - https://leetcode.com/problems/maximum-score-words-formed-by-letters/description/

class Solution:
    def canBeTaken(self, chooseFrom, curr):
        cntr = Counter(curr)
        return len(cntr - chooseFrom) == 0
    def countTotal(self, score, chars):
        total = 0
        for key, val in chars.items():
            total += sum(score[key][-val:])
        return total

    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        counter = Counter(letters)
        n = len(words)
        ans = []
        index_map = defaultdict(list)
        for i in range(len(letters)):
            index_map[letters[i]].append(score[ord(letters[i])- 97])
        for i in index_map.keys():
            index_map[i].sort()

        def backTrack(idx, chooseFrom, path):
            if idx == n:
                ans.append(path.copy())
                return
            goes_there = False
            for i in range(idx, n):
                if self.canBeTaken(chooseFrom, words[i]):
                    choose = chooseFrom - Counter(words[i])
                    path.append(words[i])
                    goes_there = True
                    backTrack(i + 1, choose, path)
                    path.pop()
            if path and not goes_there:
                ans.append(path.copy())

        backTrack(0, counter, [])
        max_count = 0
        for child in ans:
            string = Counter(''.join(child))        
            max_count = max(max_count, self.countTotal(index_map, string))
        
        return max_count