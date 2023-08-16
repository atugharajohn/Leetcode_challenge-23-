# problem:
# https://leetcode.com/problems/removing-stars-from-a-string/

# solution:
class Solution:
    def removeStars(self, s: str) -> str:
        word=[]
        for i in range (len(s)):
            if ((s[i]=="*")&(word!="")):
                word.pop()
            else:
                word.append(s[i]) 
        sn =''
        for i in word:
            sn+=i
        return sn