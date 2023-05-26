# problem:
# https://leetcode.com/problems/shortest-bridge/

# solution:
class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        N = len(grid)
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        def inbound(r, c):
            return 0 <= r < N and 0 <= c < N

        start = None
        for i in range(N):
            for j in range(N):
                if grid[i][j]:
                    start = (i, j)
                    break
            if start: break

        def bfs(turn, queue):
            count = -1
            while queue:
                M = len(queue)
                count += 1
                for _ in range(M):
                    r, c = queue.popleft()
                    if turn:
                        store.append((r,c))
                    for x, y in directions:
                        nr = x + r
                        nc = y + c
                        if inbound(nr, nc) and (nr, nc) not in visited:
                            if turn and grid[nr][nc]:
                                queue.append((nr, nc))
                                visited.add((nr, nc))
                            if not turn and grid[nr][nc]:
                                return count
                            if not turn and not grid[nr][nc]:
                                queue.append((nr, nc))
                                visited.add((nr, nc))
            return count
        visited = set()
        visited.add((start))
        store = deque([])
        bfs(True,deque([start]))
        return bfs(False, store)