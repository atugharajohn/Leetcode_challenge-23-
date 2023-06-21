# problem:
# https://leetcode.com/problems/number-of-increasing-paths-in-a-grid/

# solution:
class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        mod = 10**9+7       
        n = len(grid)        
        m = len(grid[0])       
        dp = [[-1 for _ in range(m)] for _ in range(n)]
        
        def solve(row,col,grid,prev,dp):
          
            if row < 0 or col<0 or row >= len(grid) or col >= len(grid[0]) or grid[row][col] <= prev:
                return 0
            if dp[row][col] != -1: 
                return dp[row][col]
            directions=[[1,0],[-1,0],[0,-1],[0,1]]            
            total=1
            for dir in directions:
                new_row=row+dir[0]
                new_col=col+dir[1]
                total += solve(new_row,new_col,grid,grid[row][col],dp)
            dp[row][col] = total
            return total
      
        res=0
        for row in range(n):
            for col in range(m):
                res += solve(row,col,grid,-1,dp)
        return res % mod

                    
                


                    
                
