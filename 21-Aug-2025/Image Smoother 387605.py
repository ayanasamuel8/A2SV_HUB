# Problem: Image Smoother - https://leetcode.com/problems/image-smoother/description/

class Solution:
    def isValid(self, newx,newy,n,m):
        return newx>=0 and newy>=0 and newy<m and newx<n
    def sumUp(self,row,col,img,drxn,n,m):
        valids=[img[row+i][col+j] for i,j in drxn if self.isValid(row+i,col+j,n,m)]
        return sum(valids)//len(valids)
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        drxn=[[0,0],[0,1],[1,0],[-1,0],[0,-1],[1,1],[-1,-1],[-1,1],[1,-1]]
        n,m=len(img),len(img[0])
        answer = [[0]*m for _ in range(n)]
        for row in range(n):
            for col in range(m):
                answer[row][col]=self.sumUp(row,col,img,drxn,n,m)
        return answer