# Problem: Keys and Rooms - https://leetcode.com/problems/keys-and-rooms/

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = [False] * (len(rooms))

        unlocked = deque([0])
        while unlocked:
            key = unlocked.popleft()
            visited[key] = True
            for new_key in rooms[key]:
                if not visited[new_key]:
                    unlocked.append(new_key)
        
        return all(visited)