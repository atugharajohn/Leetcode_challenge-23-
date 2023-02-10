# problem:
# https://leetcode.com/problems/find-all-anagrams-in-a-string/description/

# solution:
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        l1=[0 for i in range(26)] # list for counting characters of p
        l2=[0 for i in range(26)] # list for counting characters of s
        x=ord('a') # Just to subtract with ord of s and get index
        for i,j in zip(p,s):
            l1[ord(i)-x]+=1       # count 1 for each character in s
            l2[ord(j)-x]+=1       # count 1 for each character in p

        np=len(p)
        ns=len(s)
        point=0       # to point at the last
        all_starts=[]        # collect all starting points in array
        while point+np<=ns:
            if l1==l2: 
                all_starts.append(point)
            l2[ord(s[point])-x]-=1
            l2[ord(s[(point+np)%ns])-x]+=1
            point+=1
        return all_starts