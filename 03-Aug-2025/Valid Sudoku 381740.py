# Problem: Valid Sudoku - https://leetcode.com/problems/valid-sudoku/

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        sub_matrix=[[0]*9 for _ in range(9)]
        for i in range(9):
            row,col=[0]*9,[0]*9
            for j in range(9):
                if board[i][j].isdigit():
                    curr=int(board[i][j])
                    sub_index=(i//3)*3+(j//3)
                    if row[curr-1]: return False
                    row[curr-1]+=1
                    if sub_matrix[sub_index][curr-1]: return False
                    sub_matrix[sub_index][curr-1]+=1
                if board[j][i].isdigit():
                    curr=int(board[j][i])
                    col[curr-1]+=1
                    if col[curr-1]>1: return False
        return True