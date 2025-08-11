# Problem: Diagonal Traverse - https://leetcode.com/problems/diagonal-traverse/

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        ans = []
        n,m = len(mat), len(mat[0])
        i,j =0,0
        for _ in range(n+m):
            while i>=0 and j<m:
                ans.append(mat[i][j])
                i-=1
                j+=1
            i+=1
            if j>=m: 
                j-=1
                i+=1
            while j>=0 and i<n:
                ans.append(mat[i][j])
                i+=1
                j-=1
            j+=1
            if i>=n: 
                i-=1
                j+=1
        return ans