# problem:
# https://leetcode.com/problems/word-pattern/

# solution:
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split(' ')
        if len(pattern)!=len(s): return False

        d1 = {}
        d2 = {}
        for k,v in zip(pattern,s):
            try:
                if d1[k]!=v: return False
            except: 
                try:
                    if d2[v]!=k: return False
                except:
                    d1[k]=v
                    d2[v]=k
        return True