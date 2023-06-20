# problem:
# https://leetcode.com/problems/shortest-path-in-binary-matrix/

# solution:
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        N = len(grid)
        if grid[0][0] or grid[N-1][N-1]:
            return -1
        bfs = [(0, 0)]
        grid[0][0] = 1
        path = 0
        while bfs:
            path += 1
            new = []
            for i, j in bfs:
                if i == j == N - 1:
                    return path
                for di, dj in filter(any, itertools.product((-1, 0, 1), repeat=2)):
                    ni, nj = di + i, dj + j
                    if 0 <= ni < N and 0 <= nj < N and not grid[ni][nj]:
                        new.append((ni, nj))
                        grid[ni][nj] = 1
            bfs = new
        return -1