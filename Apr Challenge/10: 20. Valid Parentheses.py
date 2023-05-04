# problem:
# https://leetcode.com/problems/valid-parentheses/

# solution:
class Solution:
    def isValid(self, s: str) -> bool:
        l=[]
        d={'(':')','{':'}','[':']'}
        a=0
        for i in s:
            if i in '({[':
                l.append(i)
                a+=1
            else:
                if not l: return False
                x = l.pop()
                a-=1
                if d[x]!=i: return False
        if a: return False
        return True