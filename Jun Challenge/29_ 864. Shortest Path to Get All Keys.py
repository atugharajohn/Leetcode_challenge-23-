# problem:
# https://leetcode.com/problems/shortest-path-to-get-all-keys/

# solution:
class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        m, n = len(grid), len(grid[0])
        
        ii = jj = total = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "@": ii, jj = i, j
                elif grid[i][j].islower(): total += 1
        
        ans = 0
        seen = {(ii, jj, 0)}
        queue = [(ii, jj, 0)]
        while queue: 
            newq = []
            for i, j, keys in queue: 
                if keys == (1 << total) - 1: return ans 
                for ii, jj in (i-1, j), (i, j-1), (i, j+1), (i+1, j): 
                    if 0 <= ii < m and 0 <= jj < n and grid[ii][jj] != "#": 
                        kk = keys 
                        if grid[ii][jj].islower(): kk |= 1 << ord(grid[ii][jj]) - 97
                        if (ii, jj, kk) in seen or grid[ii][jj].isupper() and not kk & (1 << ord(grid[ii][jj])-65): continue 
                        newq.append((ii, jj, kk))
                        seen.add((ii, jj, kk))
            ans += 1
            queue = newq
        return -1