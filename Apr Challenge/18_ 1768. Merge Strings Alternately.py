# problem:
# https://leetcode.com/problems/merge-strings-alternately/

# solution:
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i=0
        n=min(len(word1),len(word2))
        s=''
        while i<n:
            s+=word1[i]+word2[i]
            i+=1
        s+=word1[i:]+word2[i:]
        return s
