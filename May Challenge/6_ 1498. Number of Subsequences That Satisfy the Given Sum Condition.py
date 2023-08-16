# problem:
# https://leetcode.com/problems/number-of-subsequences-that-satisfy-the-given-sum-condition/

# solution:
class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        s=0
        e=len(nums)-1
        count = 0
        while s <= e:
            if nums[s] + nums[e] <= target:
                count+=2**(e-s)
                s+=1
            else:
                e-=1
        return count %(10**9+7)