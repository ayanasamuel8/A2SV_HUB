# Problem: Find the Punishment Number of an Integer - https://leetcode.com/problems/find-the-punishment-number-of-an-integer/description/

class Solution:
    def partition_number(self, s, index, path, result):
        if index == len(s):
            result.add(sum(int(num) for num in path))
            return

        for i in range(index, len(s)):  
            num = s[index:i + 1]
            self.partition_number(s, i + 1, path + [num], result) 
    
    def punishmentNumber(self, n: int) -> int:
        count = 0
        for i in range(1, n + 1):
            set1 = set()
            self.partition_number(str(i * i), 0, [], set1)
            if i in set1:
                count += i * i
        return count
