# problem:
# https://leetcode.com/problems/minimum-size-subarray-sum/

# solution:
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l=0     #declaring a left variable starting at 0
        ans=len(nums)+1  #setting a defult value of ans
        s=0     #initial sum of the subarrays
        for r in range(len(nums)):   #iterating the right till last
            s+=nums[r]   # will add the right element to the sum
            if s>=target:   #add to answer if target is fulfilled
                ans=min(ans,r-l+1)   #minimum of answer is taken
            while s>target:  #we will shift the right till targetnot satisfied
                s-=nums[l]
                l+=1
                if s>=target:
                    ans=min(ans,r-l+1)   #will add the target fulfilled
        return ans if ans<len(nums)+1 else 0

##Upvote if you find the solution helpful