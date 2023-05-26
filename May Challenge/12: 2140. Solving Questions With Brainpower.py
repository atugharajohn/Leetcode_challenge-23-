# problem:
# https://leetcode.com/problems/solving-questions-with-brainpower/

# solution:
class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        res=[0]*(len(questions)+1)
        for i in range(len(questions)-1,-1,-1):
            point,solve=questions[i][0],questions[i][1]
            res[i]=max(point+res[min(solve+i+1,len(questions))],res[i+1])
        return res[0]
            