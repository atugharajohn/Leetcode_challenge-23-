# problem:
# https://leetcode.com/problems/number-of-enclaves/

# solution:
class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        def dfs(x,y):
            grid[x][y]=0
            for i,j in directions:
                a=i+x
                b=j+y
                if(0<=a<self.m and 0<=b<self.n and grid[a][b]==1):
                    dfs(a,b)

        self.m=len(grid)
        self.n=len(grid[0])
        directions=[[0,1],[1,0],[0,-1],[-1,0]]
        for i in range(self.m):
            if(grid[i][0]!=0):
                dfs(i,0)
            if(grid[i][self.n-1]!=0):
                dfs(i,self.n-1)
        
        for j in range(self.n):
            if(grid[0][j]!=0):
                dfs(0,j)
            if(grid[self.m-1][j]!=0):
                dfs(self.m-1,j)

        ans=0
        for i in range(self.m):
            for j in range(self.n):
                if(grid[i][j]==1):
                    ans+=1
        return ans