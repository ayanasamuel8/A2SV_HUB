# Problem: Restore IP Addresses - https://leetcode.com/problems/restore-ip-addresses/

class Solution:
    def backTrack(self, string, count, path):
        if count >= 3:
            if string and int(string) <= 255 and len(str(int(string))) == len(string):
                path.append(string)
                self.result.append('.'.join(path))
                path.pop()
            return
        start = ''
        
        for i in range(min(len(string),3)):
            start += string[i]
            if int(start) > 255 or len(str(int(start))) != len(start):
                return
            path.append(start)
            self.backTrack(string[i + 1:], count + 1, path)
            path.pop()

    def restoreIpAddresses(self, s: str) -> List[str]:
        self.result = []
        self.backTrack(s, 0, [])
        return self.result