# Problem: Rabbits in Forest - https://leetcode.com/problems/rabbits-in-forest/

class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        counter = Counter(answers)
        rabbits = 0

        for key, val in counter.items():
            if key == 0:
                rabbits += val
            else: 
                if val != key + 1:
                    rabbits += (key + 1) * ceil((val / (key + 1)))
                else:
                    rabbits += key + 1
        
        return rabbits