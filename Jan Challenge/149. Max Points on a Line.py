# problem:
# https://leetcode.com/problems/max-points-on-a-line/

# solution:
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        m = {}
        n = len(points)
        if n==1: return 1
        for i in range(n-1):
            for j in range(i+1,n):
                x1 = points[i][0]
                y1 = points[i][1]
                x2 = points[j][0]
                y2 = points[j][1]
                try:
                    m_ = (y2-y1)/(x2-x1)
                except:
                    m_ = 9999.999
                c = y2-m_*x2
                try:
                    m[(m_,c)].add((x1,y1))
                    m[(m_,c)].add((x2,y2))
                except:
                    m[(m_,c)]=set()
                    m[(m_,c)].add((x1,y1))
                    m[(m_,c)].add((x2,y2))
        mx = -99999999999
        print(m)
        for i in m:
            if len(m[i])>mx:
                mx = len(m[i])
        return mx
        