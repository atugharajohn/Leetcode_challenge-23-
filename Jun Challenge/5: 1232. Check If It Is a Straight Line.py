# problem:
# https://leetcode.com/problems/check-if-it-is-a-straight-line/

# solution:
class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        n = len(coordinates)
        x1, x2 = coordinates[0][0], coordinates[1][0]
        y1, y2 = coordinates[0][1], coordinates[1][1]
        dx = x2 - x1
        dy = y2 - y1

        for i in range(2,n):
            x3, y3 = coordinates[i][0], coordinates[i][1]
            if (dx * (y3-y2)) != (dy * (x3-x2)):
                return False
        return True
