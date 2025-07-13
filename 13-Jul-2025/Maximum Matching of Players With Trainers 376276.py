# Problem: Maximum Matching of Players With Trainers - https://leetcode.com/problems/maximum-matching-of-players-with-trainers/

class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        left = right = 0
        n, m = len(players), len(trainers)
        
        while left < n and right < m:
            if players[left] <= trainers[right]:
                left += 1
            right += 1
        
        return left