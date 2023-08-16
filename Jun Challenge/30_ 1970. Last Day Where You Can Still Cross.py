# problem:
# https://leetcode.com/problems/last-day-where-you-can-still-cross/

# solution:
class Solution:
    def is_possible(self, mid, n, m, cells):
        grid = [[0] * m for _ in range(n)]
        for i in range(mid):
            row, col = cells[i]
            grid[row - 1][col - 1] = 1
        
        # Check if there is a path from the first row to the last row
        visited = set()
        stack = [(0, col) for col in range(m) if grid[0][col] == 0]
        
        while stack:
            row, col = stack.pop()
            if row == n - 1:
                return True
            
            if (row, col) in visited:
                continue
            visited.add((row, col))
            
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                new_row, new_col = row + dx, col + dy
                if 0 <= new_row < n and 0 <= new_col < m and grid[new_row][new_col] == 0:
                    stack.append((new_row, new_col))
        
        return False

    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        left, right = 1, len(cells)
        result = -1
        
        while left <= right:
            mid = left + (right - left) // 2
            if self.is_possible(mid, row, col, cells):
                result = mid
                left = mid + 1
            else:
                right = mid - 1
        
        return result