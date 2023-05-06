# problem:
# https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/

# solution:
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vovels = {"a", "e","i","o","u"}
        ans =0
        cur=0
        for index , value in enumerate(s):

            if value in vovels:
                cur +=1
            
            if index >= k and s[index-k] in vovels:
                cur -=1
            
            ans = max(ans,cur)
        return ans

