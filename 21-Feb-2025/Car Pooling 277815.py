# Problem: Car Pooling - https://leetcode.com/problems/car-pooling/description/

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        locations = [0]*(1001)
        for k,x,y in trips:
            locations[x] += k
            locations[y] -= k
        for i in range(1,1001):
            locations[i] += locations[i - 1]

        return max(locations) <= capacity