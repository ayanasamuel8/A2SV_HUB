# Problem: Asteroid Collision - https://leetcode.com/problems/asteroid-collision/

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for asteroid in asteroids:
            if asteroid < 0:
                while stack and stack[-1] > 0 and stack[-1] < abs(asteroid):
                    stack.pop()
                if stack and stack[-1] > 0 and stack[-1] == abs(asteroid):
                    stack.pop()
                    continue
                if stack and stack[-1] > abs(asteroid):
                    continue
            stack.append(asteroid)
        
        return stack