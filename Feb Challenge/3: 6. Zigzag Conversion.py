# problem:
# https://leetcode.com/problems/zigzag-conversion/description/

# solution:
class Solution:
    def convert(self, s: str, n: int) -> str:
        x,l= 0,[]
        flag = True # True for increment, False for decrement
        for i in range(len(s)):
            try: l[x].append(s[i])
            except: l.append([s[i]])

            if flag:
                x+=1
                if x==n-1: flag = False
            else:
                x-=1
                if x==0: flag = True
        return ''.join(map(lambda x: ''.join(x),l))