# problem:
# https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/

# solution:
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        n = len(points)
        if n==1: return 1
        l = sorted(points)
        c = 1
        x = l[0][1]
        y = l[0][0]
        print(l)
        for i in l[1:]:
            y = max(y,i[0])
            if x<y:
                c+=1
                x = i[1]
            else:
                x = min(x,i[1])
        return c
