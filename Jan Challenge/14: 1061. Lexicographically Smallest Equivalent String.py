# problem:
# https://leetcode.com/problems/lexicographically-smallest-equivalent-string/

# solution:
class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        a = []
        for i,j in zip(s1,s2):
            i_s1={i}
            j_s2={j}
            common=set()
            for x in a:
                if i in x:
                    i_s1=x
                    i_s1.add(j)
                if j in x:
                    j_s2=x
                    j_s2.add(i)
            common = i_s1.union(j_s2)
            try:
                a.remove(i_s1)
                i_s1 = None
            except: ''
            try:
                a.remove(j_s2)
                j_s2=None
            except:''
            a.append(common)

        for i in a:
            for j in a:
                if i!=j and len(i.intersection(j))>0:
                    c=i.union(j)
                    a.append(c)
                    try: a.remove(i)
                    except: ''
                    try: a.remove(j)
                    except: ''
                    
        d = {}
        for i in a:
            x=min(i)
            for j in list(i):
                d[j]=x
        a = ''
        for i in baseStr:
            try:
                a=a+d[i]
            except:
                a=a+i
        return a                
