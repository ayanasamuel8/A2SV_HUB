# Problem: Detonate the Maximum Bombs - https://leetcode.com/problems/detonate-the-maximum-bombs/description/

class Solution:
    def convertToGraph(self, bombs):
        detonations = defaultdict(lambda: [])
        for i in range(len(bombs)):
            for j in range(len(bombs)):
                if j != i:
                    bomb1 = bombs[i]
                    bomb2 = bombs[j]
                    rowDist = abs(bomb1[0] - bomb2[0])
                    colDist = abs(bomb1[1] - bomb2[1])
                    dist = sqrt(rowDist**2 + colDist**2)
                    if dist <= bomb1[2]:
                        detonations[i].append(j)
        return detonations
    def dfs(self, bomb, score):
        self.log.append(bomb)
        detonations = list(filter(lambda b: b not in self.detonated, self.ranges[bomb]))
        self.detonated = self.detonated.union(detonations)
        if not detonations:
            return len(self.detonated)
        else:
            scores = []
            for b in detonations:
                scores.append(self.dfs(b, score + len(detonations)))
            return max(scores)
    def maximumDetonation(self, bombs: list[list[int]]) -> int:
        scores = []
        self.ranges = self.convertToGraph(bombs)
        for i in range(len(bombs)):
            self.detonated = {i}
            self.log = []
            scores.append(self.dfs(i, 1))
        return max(scores)