# problem:
# https://leetcode.com/problems/palindrome-partitioning/

# solution:
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res=[]
        part=[]
        def dfs(i):
            if i>=len(s):
                res.append(part.copy())
                return 
            for j in range(i,len(s)):
                if s[i:j+1]==s[i:j+1][::-1]:
                    part.append(s[i:j+1])
                    dfs(j+1)
                    part.pop()
        dfs(0)
        return res