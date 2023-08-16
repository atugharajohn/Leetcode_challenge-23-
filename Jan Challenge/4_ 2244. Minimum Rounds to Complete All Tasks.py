# problem:
# https://leetcode.com/problems/minimum-rounds-to-complete-all-tasks/

# solution:
class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        d = {}
        for i in tasks:
            try:
                d[i]+=1
            except: 
                d[i]=1
        c = 0
        d = list(d.values())
        for i in d:
            if i == 1: return -1
            c = c + int((i+2)/3)
        return c