# problem:
# https://leetcode.com/problems/maximum-sum-circular-subarray/

# solution:
class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        max_sum=nums[0]
        min_sum=nums[0]
        current_sum_max=0
        current_sum_min=0
        total_sum=0
        for i in range(len(nums)):
            total_sum+=nums[i]
            current_sum_max=max(nums[i],current_sum_max+nums[i])
            current_sum_min=min(nums[i],current_sum_min+nums[i])
            max_sum=max(current_sum_max,max_sum)
            min_sum=min(current_sum_min,min_sum)
        return max(max_sum,total_sum-min_sum) if max_sum>0 else max_sum