# Problem: X of a Kind in a Deck of Cards - https://leetcode.com/problems/x-of-a-kind-in-a-deck-of-cards/

class Solution:
    def euclidean(self, a, b):
        if b == 0:
            return a
        temp = b
        b = a % b
        a = temp
        return self.euclidean(a, b)
        
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        cntr = Counter(deck)
        values = list(cntr.values())
        gcd = values[0]
        for val in values:
            gcd = self.euclidean(gcd, val)
        
        return gcd > 1