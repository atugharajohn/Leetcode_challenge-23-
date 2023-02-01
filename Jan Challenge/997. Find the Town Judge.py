# problem:
# https://leetcode.com/problems/find-the-town-judge/

# solution:
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        l=[[0,0] for x in range(n+1)]
        for i in trust:
            l[i[1]][1]+=1
            l[i[0]][0]+=1
        for i in range(1,len(l)):
            if l[i][0]==0 and l[i][1]==n-1:
                return i    
        return -1        