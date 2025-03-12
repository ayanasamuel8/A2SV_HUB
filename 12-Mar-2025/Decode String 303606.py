# Problem: Decode String - https://leetcode.com/problems/decode-string/

class Solution:
    def decodeString(self, s: str) -> str:
        def decode(s):

            string = []
            i = 0
            count = -1
            while i < (len(s)):

                if s[i].isdigit():

                    num = 0
                    while s[i].isdigit():
                        num = num * 10 + int(s[i])
                        i += 1

                    recived, count = decode(s[i + 1:])
                    string.extend( recived * num)

                elif s[i] == ']':
                    return [string, i + 1]
                else:
                    string.append(s[i])
                if count != -1:
                    i += count
                    count = -1
                i += 1

            return [string, i]
            
        return ''.join(decode(s)[0])