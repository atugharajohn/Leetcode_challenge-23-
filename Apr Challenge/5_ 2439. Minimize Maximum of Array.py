# problem:
# https://leetcode.com/problems/minimize-maximum-of-array/

# solution:
class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        i, n = 0, len(nums)
        minmaxnum = nums[0]
        total = 0

        for i, num in enumerate(nums):
            total += num
            minmaxnum = max(minmaxnum, math.ceil(total/(i+1)))
        
        return minmaxnum