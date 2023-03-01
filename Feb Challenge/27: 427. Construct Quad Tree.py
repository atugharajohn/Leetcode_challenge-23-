# problem:
# https://leetcode.com/problems/construct-quad-tree/

# solution:
class Solution:
    def construct(self, grid: List[List[int]]):
        def dfs(x = 0, y = 0, n = len(grid)):
            if all (grid[i+x][j+y] == grid[x][y]
                    for i in range(n) for j in range(n)):
                return Node(grid[x][y] == 1, True)
            n//= 2                                              
            return Node(False, False, dfs(x,y,n), dfs(x,y+n,n), dfs(x+n,y,n), dfs(x+n,y+n,n))
        return dfs() 