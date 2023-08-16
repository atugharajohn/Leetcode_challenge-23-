# problem:
# https://leetcode.com/problems/minimum-flips-to-make-a-or-b-equal-to-c/

# solution:
class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        n1=0
        n2=0
        n3=0
        res=0
        while(a!=0 or b!=0 or c!=0):
            n1=a&1
            n2=b&1
            n3=c&1
            if(n3==0):
                if(n1==1):
                    res+=1
                if(n2==1):
                    res+=1
            else:
                if(n1==0 and n2==0):
                    res+=1
            a>>=1
            b>>=1
            c>>=1
        return res
