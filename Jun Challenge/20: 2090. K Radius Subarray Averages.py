# problem:
# https://leetcode.com/problems/k-radius-subarray-averages/

# solution:
class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        ans = [-1]*len(nums)
        rsm = 0 # range sum
        for i, x in enumerate(nums): 
            rsm += x
            if i >= 2*k+1: rsm -= nums[i-(2*k+1)]
            if i+1 >= 2*k+1: ans[i-k] = rsm//(2*k+1)
        return ans 
