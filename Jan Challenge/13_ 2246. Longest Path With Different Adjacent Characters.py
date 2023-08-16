# problem:
# https://leetcode.com/problems/longest-path-with-different-adjacent-characters/

# solution:
class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        t={}
        for i in range(1,len(parent)):
            if parent[i] not in t:
                t[parent[i]]=[i]
            else:
                t[parent[i]].append(i)
            
        self.ans=1
        def fun(i):
            if i not in t:
                return 1
            res = 1
            for j in t[i]:
                length=fun(j)
                if s[i] != s[j]:
                    self.ans = max(self.ans,length+res)
                    res = max(res,length+1)
            return res
        
        fun(0)
        return self.ans