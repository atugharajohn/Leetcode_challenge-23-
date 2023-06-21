# problem:
# https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/

# solution:
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        c=0
        for row in grid:
            for i in row[::-1]:
                if i<0: c+=1
                else: break
        return c