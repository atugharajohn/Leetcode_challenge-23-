# problem:
# https://leetcode.com/problems/number-of-longest-increasing-subsequence/

# solution:
class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        
        dp=[1]*len(nums)

        path=[1]*len(nums)
        lis=1
        for i in range(len(nums)-1,-1,-1):
            
            p=1
            for j in range (i,len(nums)):
                if nums[i]<nums[j] and dp[i] <= 1+dp[j]:

                    if dp[i]==1+dp[j]:
                        p+=path[j]   
                    else:
                        dp[i]=1+dp[j]
                        p=path[j]
                    
                    lis=max(dp[i],lis)
                    
                    path[i]=p
                
        return sum( path[i] for i,n in enumerate(dp)  if n ==lis)