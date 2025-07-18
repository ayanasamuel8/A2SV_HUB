# Problem: Robot Collisions - https://leetcode.com/problems/robot-collisions/

class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        stack = []
        sorted_arr = sorted(zip(positions, healths, directions, range(len(positions))))
        sorted_arr = [list(item) for item in sorted_arr]
        n = len(positions)
        for i in range(n):
            if sorted_arr[i][2] == 'L':
                while stack and stack[-1][0] == 'R' and stack[-1][1] < sorted_arr[i][1]:
                    sorted_arr[i][1] -= 1
                    stack.pop()
                if stack and stack[-1][0] == 'R' and stack[-1][1] == sorted_arr[i][1]:
                    stack.pop()
                    continue
                if stack and stack[-1][0] == 'R' and stack[-1][1] > sorted_arr[i][1]:
                    stack[-1][1] -= 1
                    continue
                stack.append(['L', sorted_arr[i][1], sorted_arr[i][3]])
            else:
                stack.append(['R', sorted_arr[i][1], sorted_arr[i][3]])
        stack.sort(key=lambda x: x[2])
        return [se for [fi, se, _] in stack]
                