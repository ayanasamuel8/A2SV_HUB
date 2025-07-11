# Problem: Meeting Rooms III - https://leetcode.com/problems/meeting-rooms-iii/

class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        used_rooms = defaultdict(int)
        unused = list(range(n))
        heapify(unused)
        being_used = []  # (end_time, room_index)
        meetings.sort()
        
        for start, end in meetings:
            duration = end - start
            
            while being_used and being_used[0][0] <= start:
                _, room = heappop(being_used)
                heappush(unused, room)

            if unused:
                room = heappop(unused)
                heappush(being_used, (end, room))
            else:
                end_time, room = heappop(being_used)
                heappush(being_used, (end_time + duration, room))
                end = end_time + duration
            
            used_rooms[room] += 1
        
        max_count = -1
        answer = -1
        for room in range(n):
            if used_rooms[room] > max_count or (used_rooms[room] == max_count and room < answer):
                max_count = used_rooms[room]
                answer = room
        return answer
