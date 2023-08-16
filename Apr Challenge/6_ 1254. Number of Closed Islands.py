# problem:
# https://leetcode.com/problems/number-of-closed-islands/

# solution:
class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        row,col=len(grid),len(grid[0])
        visit=set()
        count=0
        def dfs(r,c):
            if (r<0 or c<0 or r==row or c==col):
                return 0
            if grid[r][c]==1 or (r,c) in visit:
                return 1
            visit.add((r,c))
            return min(dfs(r-1,c),dfs(r+1,c),dfs(r,c-1),dfs(r,c+1))
        
        for r in range(row):
            for c in range(col):
                if not grid[r][c] and (r,c) not in visit:
                    count += dfs(r,c)
        
        return count