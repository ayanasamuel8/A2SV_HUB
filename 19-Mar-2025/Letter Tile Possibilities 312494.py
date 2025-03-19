# Problem: Letter Tile Possibilities - https://leetcode.com/problems/letter-tile-possibilities/description/

class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        tiles = sorted(tiles)
        result = []
        used = [False] * len(tiles)
        cnt = 0
        def backTrack(path):
            nonlocal cnt
            cnt += 1
            if len(path) == len(tiles):
                return 
            for i in range(len(tiles)):
                if used[i]: continue
                elif i > 0 and tiles[i] == tiles[i-1] and not used[i-1]: continue
                else:
                    path.append(tiles[i])
                    used[i] = True
                    backTrack(path)
                    path.pop()
                    used[i] = False
            return 
        backTrack([])
        return cnt-1