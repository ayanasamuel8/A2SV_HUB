# Problem: Binary String With Substrings Representing 1 To N - https://leetcode.com/problems/binary-string-with-substrings-representing-1-to-n/

class Solution:
    def queryString(self, S, N):
        return all(bin(i)[2:] in S for i in range(N, N // 2, -1))