# problem:
# https://leetcode.com/problems/search-a-2d-matrix/

# solution:
class Solution:
    def searchMatrix(self, m: List[List[int]], t: int) -> bool:
        return [i for i in m if t in i]