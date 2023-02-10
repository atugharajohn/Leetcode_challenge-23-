# problem:
# https://leetcode.com/problems/fruit-into-baskets/

# solution:
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
            n=len(fruits)
            i=j=m=0
            x,y=fruits[0],-1
            while j<n:
                if fruits[j]!=x and y==-1:
                    y=fruits[j]
                elif fruits[j]!=x and fruits[j]!=y:
                    x,y=fruits[j-1],fruits[j]
                    m=max(m,j-i)
                    i=j-1
                    while fruits[i-1]==x:
                        i-=1
                j+=1
            m=max(m,j-i)
            return m