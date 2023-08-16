# problem:
# https://leetcode.com/problems/restore-the-array/

# solution:
class Solution:
    def numberOfArrays(self, s: str, k: int) -> int:
        mod=10**9+7
        # Bottom Up Approach
        dp=[0 for _ in range(len(s)+1)]
        dp[len(s)]=1
        for i in range(len(s)-1,-1,-1):
            if s[i]=='0':
                continue
            for j in range(i,min(i+32,len(s))):
                if int(s[i:j+1])>k:
                    break
                dp[i]+=dp[j+1]%mod
        return dp[0]%mod