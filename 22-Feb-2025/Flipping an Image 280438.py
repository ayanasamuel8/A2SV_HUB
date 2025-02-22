# Problem: Flipping an Image - https://leetcode.com/problems/flipping-an-image/description/

class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        n=len(image)
        answer=[[1^image[i][n-j-1] for j in range(n)] for i in range(n)]
        return answer