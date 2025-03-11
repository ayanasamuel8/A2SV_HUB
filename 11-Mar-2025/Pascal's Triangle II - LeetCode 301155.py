# Problem: Pascal's Triangle II - LeetCode - https://leetcode.com/problems/pascals-triangle-ii/

class Solution:
    def generatePascals(self,path, index, rowIndex):
        if index == rowIndex + 1: return path
        lst = [1]
        for i in range(1, len(path)):
            lst.append(path[i] + path[i - 1])
        lst.append(1)
        return self.generatePascals(lst,index + 1, rowIndex)
    def getRow(self, rowIndex: int) -> List[int]:
        pascals = [1]
        generated = self.generatePascals(pascals, 1, rowIndex)
        return generated