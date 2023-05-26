# problem:
# https://leetcode.com/problems/matrix-diagonal-sum/

# solution:
class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        sum,a,b = 0,0,len(mat)-1
        for i in range(len(mat)):
            for j in range(len(mat)):
                if i == j:
                    sum+=mat[i][j]
                elif(i+j == len(mat)-1):
                    sum +=mat[i][j] 
        
        return sum